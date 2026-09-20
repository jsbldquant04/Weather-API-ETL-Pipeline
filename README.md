# 🌦️ Weather API ETL Pipeline

Author: Joshua Bloodymier Salvino
Date: September 20, 2026

An end-to-end **ETL (Extract, Transform, Load) pipeline** that retrieves weather forecast data from the **Open-Meteo REST API**, processes and validates the data using Python and Pandas, stores the results in a **SQLite database**, and presents the results through an interactive **Plotly dashboard**.

This project demonstrates a practical data engineering workflow, from API ingestion and data transformation to data-quality validation, database storage, SQL analytics, and visualization.

---

## 🏗️ Architecture

```text
                Open-Meteo API
                      │
                      ▼
              Python / Requests
                      │
                      ▼
                   Extract
                      │
                      ▼
             Transform / Clean
                      │
                      ▼
             Data Quality Checks
                      │
                      ▼
                  SQLite
                      │
                 ┌────┴────┐
                 ▼         ▼
              SQL      Pandas
                 │         │
                 └────┬────┘
                      ▼
              Plotly Dashboard
```

---

## 🚀 Features

* 🌐 Extract weather data from a REST API
* 🔄 Transform nested JSON responses into structured tabular data
* 🧹 Clean and standardize weather observations
* 🧮 Perform feature engineering
* ✅ Run automated data-quality checks
* 🗄️ Store processed data in SQLite
* 🔍 Query data using SQL and Pandas
* 📊 Build an interactive Plotly dashboard
* ☁️ Develop and run the project in Google Colab
* 🔁 Reusable ETL pipeline structure

---

## 🛠️ Technologies

| Technology       | Purpose                          |
| ---------------- | -------------------------------- |
| **Python**       | Pipeline development             |
| **Requests**     | API requests                     |
| **Pandas**       | Data transformation and analysis |
| **SQLite**       | Data storage                     |
| **SQL**          | Data querying and analytics      |
| **Plotly**       | Interactive visualization        |
| **Google Colab** | Development and execution        |

---

## 📂 Project Structure

```text
weather-api-etl/
│
├── data/
│   └── weather.db
│
├── notebooks/
│   └── weather_etl_demo.ipynb
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── pipeline.py
│
├── dashboard/
│   └── dashboard.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🔄 ETL Workflow

### 1. Extract

The pipeline sends requests to the Open-Meteo API and retrieves weather forecast data in JSON format.

```text
City
 ↓
Geocoding API
 ↓
Latitude / Longitude
 ↓
Weather API
 ↓
JSON Response
```

---

### 2. Transform

The raw API response is converted into a structured Pandas DataFrame.

Typical transformations include:

* Flattening JSON data
* Converting timestamps
* Standardizing column names
* Handling missing values
* Converting data types
* Creating derived weather features

Example:

```text
Raw JSON
   ↓
Pandas DataFrame
   ↓
Cleaned DataFrame
   ↓
Feature Engineering
```

---

### 3. Data Quality Checks

Before loading the data into the database, the pipeline performs validation checks such as:

* Missing-value detection
* Duplicate detection
* Data-type validation
* Temperature range validation
* Precipitation validation
* Timestamp validation
* Record-count validation

Example:

```python
assert df["temperature"].notna().all()
assert df["timestamp"].notna().all()
assert df["city"].notna().all()
```

These checks help prevent invalid or corrupted data from entering the database.

---

### 4. Load

The validated dataset is stored in a **SQLite database**.

```text
Clean DataFrame
      ↓
SQLite Database
      ↓
SQL Queries
      ↓
Analytics
```

SQLite provides a lightweight relational database that makes the project easy to run locally or in Google Colab without requiring a separate database server.

---

## 📊 Dashboard

The project uses **Plotly** to create an interactive weather dashboard.

The dashboard can be used to explore:

* 🌡️ Temperature trends
* 💧 Humidity
* 🌧️ Precipitation
* 🌬️ Wind speed
* ☁️ Weather conditions
* 📅 Forecast changes over time
* 🏙️ Differences between cities

---

## 🔎 Example SQL Analytics

The stored data can be queried using SQL to answer questions such as:

### Average temperature by city

```sql
SELECT
    city,
    AVG(temperature) AS average_temperature
FROM weather
GROUP BY city;
```

### Highest forecast temperature

```sql
SELECT
    city,
    timestamp,
    temperature
FROM weather
ORDER BY temperature DESC
LIMIT 10;
```

### Expected precipitation

```sql
SELECT
    city,
    SUM(precipitation) AS total_precipitation
FROM weather
GROUP BY city;
```

---

## 💡 Example Questions

The pipeline can be used to answer questions such as:

* What is the average temperature by city?
* Which city has the highest forecast temperature?
* How much precipitation is expected?
* How does humidity change over time?
* Which city has the highest wind speed?
* What are the most common weather conditions?
* How does the forecast change throughout the week?

---

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/weather-api-etl.git
cd weather-api-etl
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the ETL pipeline

```bash
python src/pipeline.py
```

The pipeline will:

```text
Extract API data
      ↓
Transform data
      ↓
Validate data
      ↓
Load into SQLite
      ↓
Run analytics
```

### 4. Open the notebook

Open:

```text
notebooks/weather-api-etl-pipeline.ipynb
```

The notebook provides a step-by-step demonstration of the complete pipeline.

---

## 📦 Requirements

Example `requirements.txt`:

```text
requests
pandas
plotly
```

SQLite is included with Python, so a separate SQLite installation is not required.

---

## 🎯 Learning Objectives

This project demonstrates several fundamental concepts used in real-world data engineering and analytics:

* REST API integration
* ETL pipeline design
* JSON processing
* Data cleaning
* Data validation
* Feature engineering
* Relational databases
* SQL analytics
* Data visualization
* Pipeline automation

The main goal is to demonstrate how **raw external data can be transformed into reliable, queryable, and visualized information**.

---

## 🔮 Future Improvements

Possible extensions include:

* [ ] Add PostgreSQL support
* [ ] Add Airflow orchestration
* [ ] Add Docker
* [ ] Add automated scheduled API extraction
* [ ] Add unit tests with `pytest`
* [ ] Add more cities and historical data
* [ ] Add logging and error handling
* [ ] Add CI/CD with GitHub Actions
* [ ] Deploy the dashboard as a web application
* [ ] Add a data-quality framework such as Great Expectations
* [ ] Add weather anomaly detection using machine learning

---

## 👨‍💻 Project Purpose

This project was built as a portfolio demonstration of an **end-to-end data pipeline**, combining API integration, Python data processing, database management, SQL analytics, data-quality validation, and interactive visualization.
