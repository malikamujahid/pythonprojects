import snowflake.connector
import os
from dotenv import load_dotenv
import logging      

load_dotenv()
logging.basicConfig(level=logging.INFO)

logging.info("Loading Snowflake connection parameters from environment variables...")

SNOWFLAKE_USER = os.getenv("user")
SNOWFLAKE_PASSWORD = os.getenv("password")
SNOWFLAKE_ACCOUNT = os.getenv("account")
SNOWFLAKE_DATABASE = os.getenv("database")
SNOWFLAKE_SCHEMA = os.getenv("schema")
SNOWFLAKE_WAREHOUSE = os.getenv("warehouse")
TABLE_NAME = os.getenv("table_name")

conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA,
    warehouse=SNOWFLAKE_WAREHOUSE
)

logging.info("Connected to Snowflake successfully.")

cursor = conn.cursor()
query = f'SELECT * FROM {SNOWFLAKE_DATABASE}.{SNOWFLAKE_SCHEMA}."{TABLE_NAME}" LIMIT 5'
logging.info(f"Executing query: {query}")

cursor.execute(query)

for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
