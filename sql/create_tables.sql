CREATE TABLE weather_hourly (
    city TEXT,
    time DATETIME,
    latitude REAL,
    longitude REAL,

    temperature_c REAL,
    humidity_pct REAL,
    feels_like_c REAL,

    precip_probability_pct REAL,
    precipitation_mm REAL,
    rain_mm REAL,

    wind_speed_kmh REAL,
    cloud_cover_pct REAL,

    weather_code INTEGER,
    weather_description TEXT,

    date DATE,
    hour INTEGER,
    day_of_week TEXT,

    is_raining INTEGER,
    temperature_difference REAL,
    is_hot INTEGER
);
