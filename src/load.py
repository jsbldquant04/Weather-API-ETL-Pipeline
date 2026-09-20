import sqlite3


def create_connection(database_path):
    """Create SQLite connection."""

    return sqlite3.connect(database_path)


def load_dataframe(
    df,
    table_name,
    connection
):
    """Load DataFrame into SQLite."""

    df.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False
    )

    connection.commit()

    print(
        f"Loaded {len(df)} rows "
        f"into {table_name}"
    )
