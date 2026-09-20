def run_quality_checks(df):

    assert len(df) > 0, \
        "Dataset is empty."

    assert df["time"].notna().all(), \
        "Missing timestamps."

    assert df["city"].notna().all(), \
        "Missing city values."

    assert df["temperature_c"].notna().all(), \
        "Missing temperature."

    assert df["humidity_pct"].between(
        0, 100
    ).all(), \
        "Invalid humidity."

    assert (
        df["precipitation_mm"] >= 0
    ).all(), \
        "Negative precipitation."

    duplicates = df.duplicated(
        subset=["city", "time"]
    ).sum()

    assert duplicates == 0, \
        "Duplicate city/time records."

    print("✅ Data quality checks passed.")

    return True
