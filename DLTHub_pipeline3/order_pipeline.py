import dlt 
from sql_database_pipeline import sql_database
import humanize 
import logging
from order_unnest import unnest_order
logging.basicConfig(level=logging.INFO)



pipeline = dlt.pipeline(
    pipeline_name="order_pipeline",
    destination="snowflake",
    dataset_name="unnest_pg_to_sf"
)

pipeline.run(unnest_order())