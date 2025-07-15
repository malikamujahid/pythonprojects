import dlt
import os
import logging
from dotenv import load_dotenv  
import snowflake.connector  

logging.basicConfig(level=logging.INFO)
load_dotenv()

logging.info("Loading Snowflake connection parameters from environment variables...")
@dlt.resource
def snowflake_data():
    SNOWFLAKE_USER = os.getenv("user")
    SNOWFLAKE_PASSWORD = os.getenv("password")
    SNOWFLAKE_ACCOUNT = os.getenv("account")
    SNOWFLAKE_DATABASE = os.getenv("database")
    SNOWFLAKE_SCHEMA = os.getenv("schema")
    SNOWFLAKE_WAREHOUSE = os.getenv("warehouse")
    table_name = os.getenv("table_name")

    if not table_name:
        raise ValueError("Missing 'table_name' environment variable.")

    logging.info("Snowflake connection parameters loaded from environment variables.")

    conn = snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        warehouse=SNOWFLAKE_WAREHOUSE
    )

    try:
        logging.info("Connected to Snowflake successfully.")
        cursor = conn.cursor()
        query = f'SELECT * FROM {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}."{table_name}" LIMIT 5'
        logging.info(f"Executing query: {query}")
        cursor.execute(query)

        columns = [col[0] for col in cursor.description]
        rows = cursor.fetchall()

        if not rows:
            logging.info("No data found in Snowflake table.")
        else:
            logging.info("Snowflake data fetched successfully.")

        for row in rows:
            yield dict(zip(columns, row))
    finally:
        cursor.close()
        conn.close()

@dlt.source
def snowflake_source():
    return snowflake_data()

if __name__ == "__main__":
    source = snowflake_source()
    for item in source.resources["snowflake_data"]:
        print(item)
        logging.info(f"Fetched item: {item}")
