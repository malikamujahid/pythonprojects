import dlt 
from sql_database_pipeline import sql_database
import humanize 
import logging

logging.basicConfig(level=logging.INFO)


import dlt
from customer_unnest import unnest_customers

pipeline = dlt.pipeline(
    pipeline_name="customer_pipeline",
    destination="snowflake",
    dataset_name="unnest_pg_to_sf"
)

pipeline.run(unnest_customers())
