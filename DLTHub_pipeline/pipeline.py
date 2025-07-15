import dlt
from clickupsource import clickup_source
from snowflakesource import snowflake_source
import logging
import duckdb
logging.basicConfig(level=logging.INFO)

pipeline= dlt.pipeline(
    pipeline_name= "clickup_snowflake_pipeline",
    destination="duckdb",
    dataset_name="clickup_snowflake_dataset"   
)
logging.info("Pipeline initialized with DuckDB destination.")


load_info_clickup = pipeline.run(clickup_source())
logging.info("ClickUp source loaded successfully.")
print("ClickUp extraction result:")
print(load_info_clickup)

load_info_snowflake = pipeline.run(snowflake_source())
logging.info("Snowflake source loaded successfully.")
print("Snowflake extraction result:")
print(load_info_snowflake)\


conn=duckdb.connect("clickup_snowflake_dataset.duckdb")
logging.info("Connected to DuckDB database.")
tables = conn.execute("SHOW TABLES").fetchall()
print(tables)