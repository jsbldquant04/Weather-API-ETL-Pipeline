from extract import (
    get_coordinates,
    get_weather_data
)

from transform import (
    transform_weather_data
)

from quality import (
    run_quality_checks
)

from load import (
    create_connection,
    load_dataframe
)


CITIES = [
    "Manila",
    "Cebu City",
    "Davao City"
]

DATABASE = "weather_etl.db"


def run_pipeline():

    all_data = []

    for city in CITIES:

        print(f"\nProcessing {city}...")

        # -------------------------
        # EXTRACT LOCATION
        # -------------------------

        location = get_coordinates(city)

        # -------------------------
        # EXTRACT WEATHER
        # -------------------------

        raw_data = get_weather_data(
            city=city,
            latitude=location["latitude"],
            longitude=location["longitude"],
            forecast_days=7
        )

        # -------------------------
        # TRANSFORM
        # -------------------------

        df = transform_weather_data(
            city,
            raw_data
        )

        all_data.append(df)

    # Combine cities
    final_df = pd.concat(
        all_data,
        ignore_index=True
    )

    # -------------------------
    # QUALITY CHECK
    # -------------------------

    run_quality_checks(final_df)

    # -------------------------
    # LOAD
    # -------------------------

    connection = create_connection(
        DATABASE
    )

    load_dataframe(
        final_df,
        "weather_hourly",
        connection
    )

    connection.close()

    print("\n✅ ETL pipeline completed.")

    return final_df


if __name__ == "__main__":
    run_pipeline()
