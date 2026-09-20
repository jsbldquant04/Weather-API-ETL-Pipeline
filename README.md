# Weather API ETL Pipeline

An end-to-end ETL pipeline that extracts weather data
from the Open-Meteo API, transforms and validates the
data using Python/Pandas, stores the results in SQLite,
and produces an interactive weather dashboard using Plotly.

## Architecture

Open-Meteo API
      ↓
Python Requests
      ↓
Extract
      ↓
Transform
      ↓
Data Quality Checks
      ↓
SQLite
      ↓
SQL / Pandas
      ↓
Plotly Dashboard

## Technologies

- Python
- REST API
- Pandas
- Requests
- SQLite
- SQL
- Plotly
- Google Colab

## Features

- API-based data extraction
- JSON transformation
- Data cleaning
- Feature engineering
- Automated data-quality checks
- SQLite data warehouse
- SQL analytics
- Interactive dashboard

## How to Run

1. Clone the repository
2. Install dependencies

pip install -r requirements.txt

3. Run the pipeline

python src/pipeline.py

4. Open the notebook

notebooks/weather_etl_demo.ipynb

## Example Questions

- What is the average temperature by city?
- Which city has the highest forecast temperature?
- How much precipitation is expected?
- What are the most common weather conditions?
- How does humidity change over time?
