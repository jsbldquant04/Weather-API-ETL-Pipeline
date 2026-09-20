-- 1. Average temperature by city
SELECT
    city,
    ROUND(AVG(temperature_c), 2) AS avg_temperature_c
FROM weather_hourly
GROUP BY city
ORDER BY avg_temperature_c DESC;


-- 2. Maximum temperature by city
SELECT
    city,
    MAX(temperature_c) AS max_temperature_c
FROM weather_hourly
GROUP BY city
ORDER BY max_temperature_c DESC;


-- 3. Minimum temperature by city
SELECT
    city,
    MIN(temperature_c) AS min_temperature_c
FROM weather_hourly
GROUP BY city
ORDER BY min_temperature_c ASC;


-- 4. Average humidity by city
SELECT
    city,
    ROUND(AVG(humidity_pct), 2) AS avg_humidity_pct
FROM weather_hourly
GROUP BY city
ORDER BY avg_humidity_pct DESC;


-- 5. Total precipitation by city
SELECT
    city,
    ROUND(SUM(precipitation_mm), 2) AS total_precipitation_mm
FROM weather_hourly
GROUP BY city
ORDER BY total_precipitation_mm DESC;


-- 6. Average wind speed by city
SELECT
    city,
    ROUND(AVG(wind_speed_kmh), 2) AS avg_wind_speed_kmh
FROM weather_hourly
GROUP BY city
ORDER BY avg_wind_speed_kmh DESC;


-- 7. Number of rainy hours by city
SELECT
    city,
    SUM(is_raining) AS rainy_hours
FROM weather_hourly
GROUP BY city
ORDER BY rainy_hours DESC;


-- 8. Most common weather condition
SELECT
    city,
    weather_description,
    COUNT(*) AS occurrence_count
FROM weather_hourly
GROUP BY city, weather_description
ORDER BY city, occurrence_count DESC;


-- 9. Average temperature by day
SELECT
    city,
    date,
    ROUND(AVG(temperature_c), 2) AS avg_temperature_c
FROM weather_hourly
GROUP BY city, date
ORDER BY city, date;


-- 10. Maximum temperature by day
SELECT
    city,
    date,
    MAX(temperature_c) AS max_temperature_c
FROM weather_hourly
GROUP BY city, date
ORDER BY city, date;


-- 11. Total rainfall by day
SELECT
    city,
    date,
    ROUND(SUM(precipitation_mm), 2) AS total_rainfall_mm
FROM weather_hourly
GROUP BY city, date
ORDER BY city, date;


-- 12. Hottest hours
SELECT
    city,
    time,
    temperature_c
FROM weather_hourly
ORDER BY temperature_c DESC
LIMIT 20;


-- 13. Hours with the highest precipitation
SELECT
    city,
    time,
    precipitation_mm
FROM weather_hourly
ORDER BY precipitation_mm DESC
LIMIT 20;


-- 14. Compare cities
SELECT
    city,
    ROUND(AVG(temperature_c), 2) AS avg_temperature_c,
    ROUND(AVG(humidity_pct), 2) AS avg_humidity_pct,
    ROUND(SUM(precipitation_mm), 2) AS total_precipitation_mm,
    ROUND(AVG(wind_speed_kmh), 2) AS avg_wind_speed_kmh,
    SUM(is_raining) AS rainy_hours
FROM weather_hourly
GROUP BY city
ORDER BY avg_temperature_c DESC;
