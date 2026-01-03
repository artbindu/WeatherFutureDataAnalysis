# Future Rainfall Data Prediction Project

**Version: 1.0.0**

Future rainfall prediction system using Artificial Neural Networks (ANN) and K-means clustering. Processes historical Indian rainfall data (1951-2017) to predict future rainfall patterns using dual ANN approaches.

## Repository

```bash
git clone https://artbindu@bitbucket.org/artbindu/dataanalysisproject_weather.git
```

## Features

- Import Excel data to MongoDB
- K-means clustering noise filtering (7 clusters)
- **ANN-I**: Predicts from same month across years
- **ANN-II**: Predicts using previous 5 months
- Matplotlib visualization comparing predictions

## Installation

**Required:**
- Python 3.12.x
- MongoDB 8.0+ Community Edition

**MongoDB Setup Resources:**
- **MongoDB Community Server**: https://www.mongodb.com/try/download/community
- **MongoDB Shell**: https://www.mongodb.com/try/download/shell
- **Robo3T** (GUI): https://github.com/Studio3T/robomongo/releases/tag/v1.4.4
- **Configuration Tutorial**: https://www.youtube.com/watch?v=tC49Nzm6SyM

**Install Python Dependencies:**
```bash
python -m pip install --upgrade pip
pip install xlrd openpyxl pymongo numpy matplotlib
```

## Quick Start

1. Start MongoDB on `localhost:27017`
2. Run: `python main.py`
3. Choose option:
   - `0` - Exit program
   - `1` - Import Excel data (optional clustering)
   - `2` - Analyze & visualize data
   - `3` - Clear database

## Configuration

Edit `src/share/config.json`:
```json
{
    "rawDataPath": {"rainfall": "data/RainFallData.xlsx"},
    "mongoConfig": {"url": "localhost:27017", "dbName": "WeatherDataAnalysis"},
    "ann": {"hiddenSize": 5, "learningRate": 0.2, "trainingIteration": 999},
    "clustering": {"noOfClusterSet": 7}
}
```

## Project Structure

```
src/
├── controller/      # Main orchestration
├── excel/           # Excel input
├── mongoo/          # MongoDB operations
├── clustering/      # K-means filtering
├── ANNalgo/         # Neural network (3 layers)
├── graph/           # Matplotlib plotting
└── share/           # Config & utilities
```

## Documentation

[Project documentation](./document/project-details.pdf)

[Project presentation](./document/project-ppt.pptx)

## Technical Details

- **ANN**: 3 hidden layers (5 neurons each), sigmoid activation
- **Clustering**: K-means with 7 clusters for outlier detection
- **Database**: MongoDB collection with Region/Year/Month/Data fields

## Troubleshooting

- Ensure MongoDB is running
- Run from project root directory
- Verify `data/RainFallData.xlsx` exists
- Uses PyMongo 3.7+ (updated from deprecated methods)
