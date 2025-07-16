import dlt 
from sql_database_pipeline import sql_database
import humanize 
import logging
import dlt
from items_unnest import unnest_items
logging.basicConfig(level=logging.INFO)


pipeline = dlt.pipeline(
    pipeline_name="items_pipeline",
    destination="snowflake",
    dataset_name="unnest_pg_to_sf"
)

pipeline.run(unnest_items())