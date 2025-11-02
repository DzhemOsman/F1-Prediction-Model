import fastf1
import pandas as pd
from pathlib import Path

# Cache für FastF1 aktivieren (beschleunigt wiederholte Abfragen)
fastf1.Cache.enable_cache('data/cache')

def fetch_session_data(year, grand_prix, session_type='R'):
    """
    Lädt Session-Daten von FastF1
    
    Args:
        year: Jahr (z.B. 2023)
        grand_prix: Grand Prix Name (z.B. 'Monaco', 'Bahrain')
        session_type: 'FP1', 'FP2', 'FP3', 'Q', 'R' (Race)
    """
    session = fastf1.get_session(year, grand_prix, session_type)
    session.load()
    return session

def extract_lap_data(session):
    """Extrahiert Rundenzeiten und relevante Features"""
    laps = session.laps
    
    # Relevante Spalten auswählen
    features = laps[[
        'Driver', 'DriverNumber', 'LapNumber', 'LapTime', 
        'Sector1Time', 'Sector2Time', 'Sector3Time',
        'Compound', 'TyreLife', 'FreshTyre',
        'Team', 'TrackStatus', 'IsPersonalBest'
    ]].copy()
    
    # LapTime in Sekunden konvertieren
    features['LapTimeSeconds'] = features['LapTime'].dt.total_seconds()
    
    return features

def save_to_csv(data, filename='f1_training_data.csv', append=False):
    """Speichert Daten in CSV"""
    filepath = Path("data/" + filename)
    
    if append and filepath.exists():
        data.to_csv(filepath, mode='a', header=False, index=False)
    else:
        data.to_csv(filepath, index=False)
    
    print(f"Daten gespeichert in: {filepath}")

# Beispiel: Daten für mehrere Rennen sammeln
def collect_season_data(year, races, output_file='f1_season_data.csv'):
    """Sammelt Daten für eine ganze Saison"""
    all_data = []
    
    for race in races:
        try:
            print(f"Lade Daten für {race} {year}...")
            session = fetch_session_data(year, race, 'R')
            lap_data = extract_lap_data(session)
            lap_data['GrandPrix'] = race
            lap_data['Year'] = year
            all_data.append(lap_data)
        except Exception as e:
            print(f"Fehler bei {race}: {e}")
    
    # Alle Daten kombinieren
    if all_data:
        combined_data = pd.concat(all_data, ignore_index=True)
        save_to_csv(combined_data, output_file)
        return combined_data
    
    return None

# Beispiel-Verwendung:
def main():
    # Einzelnes Rennen
    session = fetch_session_data(2024, 'Monaco', 'R')
    lap_data = extract_lap_data(session)
    save_to_csv(lap_data, 'monaco_2024.csv')
    
    # Mehrere Rennen
    races = ['Bahrain', 'Saudi Arabia', 'Australia', 'Japan']
    collect_season_data(2024, races, 'f1_2024_data.csv')

main()