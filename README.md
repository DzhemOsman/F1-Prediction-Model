# 🏎️ F1 Race Position Prediction Model

A machine learning project that predicts Formula 1 race finishing positions using historical race data, weather conditions, and team standings. The project implements two models: a **Neural Network (Multi-Layer Perceptron)** and a **Gradient Boosting Regressor** for comparison.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation (macOS)](#installation-macos)
- [Usage](#usage)
- [Data Sources](#data-sources)
- [Models](#models)
- [License](#license)

## 🎯 Overview

This project uses machine learning to predict the finishing positions of F1 drivers based on:

- **Grid Position** - Starting position on the race grid
- **Weather Data** - Air temperature, track temperature, humidity, and rainfall
- **Team Standings** - Team performance and points
- **Historical Performance** - Past race results from the 2024 season

The models are trained on 2024 F1 season data and tested against 2025 race results.

## ✨ Features

- 🔄 **Data Collection** - Automated F1 data collection using FastF1 API
- 🧠 **Two ML Models** - Neural Network (MLP) and Gradient Boosting Regressor
- 📊 **Visualization** - Training curves, prediction analysis, and driver error analysis
- 📈 **Model Evaluation** - MAE, MSE, and R² metrics
- 🏁 **Race Predictions** - Generate race-by-race position predictions

## 📁 Project Structure

```
F1-Prediction-Model/
├── f1_prediction.ipynb          # Main prediction notebook (training & evaluation)
├── fastf1_data_collector.ipynb  # Data collection from FastF1 API
├── requirements.txt             # Python dependencies
├── data/
│   ├── csv/                     # Processed CSV files
│   │   ├── train_race_results_2024.csv
│   │   ├── train_weather_2024.csv
│   │   ├── train_team_standings_2024.csv
│   │   ├── test_race_results_2025.csv
│   │   ├── test_weather_2025.csv
│   │   └── test_team_standings_2025.csv
│   └── cache/                   # FastF1 cache data
├── *.keras                      # Saved Keras model files
└── f1_2025_predictions.csv      # Generated predictions
```

## 🍎 Installation (macOS)

### Prerequisites

- **Python 3.9+** - Make sure Python is installed on your Mac
- **pip** - Python package manager (comes with Python)

### Step-by-Step Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/DzhemOsman/F1-Prediction-Model.git
   cd F1-Prediction-Model
   ```

2. **Create a virtual environment**

   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**

   ```bash
   source venv/bin/activate
   ```

   > 💡 You'll see `(venv)` at the beginning of your terminal prompt when activated.

4. **Install all dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   > ⏳ This may take a few minutes as it installs TensorFlow and other ML libraries.

5. **Verify installation**
   ```bash
   python -c "import tensorflow as tf; import fastf1; print('✅ All packages installed successfully!')"
   ```

### Troubleshooting

- **If TensorFlow fails to install on Apple Silicon (M1/M2/M3):**

  ```bash
  pip install tensorflow-macos tensorflow-metal
  ```

- **To deactivate the virtual environment when done:**
  ```bash
  deactivate
  ```

## 🚀 Usage

### 1. Collect F1 Data (Optional)

If you want to collect fresh data or data for different seasons:

1. Open `fastf1_data_collector.ipynb` in VS Code or Jupyter
2. Run all cells to fetch data from the FastF1 API
3. The data will be saved to `data/csv/` and cached in `data/cache/`

> 📝 Note: The repository already includes pre-collected data for 2024 (training) and 2025 (testing).

### 2. Train and Evaluate Models

1. Open `f1_prediction.ipynb` in VS Code or Jupyter
2. Run the cells sequentially:
   - **Import Data** - Loads and merges CSV files
   - **Data Preprocessing** - One-hot encoding and feature scaling
   - **Model Training** - Trains both MLP and GBR models
   - **Evaluation** - Visualizes results and calculates metrics

### 3. Understanding the Output

The notebook provides several visualizations:

- **Training Curves** - Loss and MAE over epochs
- **Prediction vs Reality** - Scatter plot comparing predictions to actual results
- **Driver Error Analysis** - Which drivers are hardest to predict
- **Race-by-Race Results** - Detailed predictions for each race

## 📊 Data Sources

All data is collected using the [FastF1](https://docs.fastf1.dev/) Python library, which provides access to official F1 timing data.

**Features used for prediction:**
| Feature | Description |
|---------|-------------|
| GridPosition | Starting position on the grid |
| AirTemp_Avg | Average air temperature during the race |
| TrackTemp_Avg | Average track temperature |
| Humidity_Avg | Average humidity percentage |
| Rainfall | Binary indicator (0 = dry, 1 = wet) |
| TeamName | The driver's team (one-hot encoded) |
| Abbreviation | Driver abbreviation (one-hot encoded) |

## 🤖 Models

### Multi-Layer Perceptron (Neural Network)

- Architecture: 128 → 64 → 32 neurons
- Regularization: L2 + Dropout (30%)
- Optimizer: Adam with learning rate scheduling
- Early stopping to prevent overfitting

### Gradient Boosting Regressor

- 200 estimators
- Learning rate: 0.05
- Max depth: 4
- Generally provides more stable predictions

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Made with ❤️ (+prompt) by [Dzhem Osman](https://github.com/DzhemOsman)**
