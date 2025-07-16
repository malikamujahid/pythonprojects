import dlt 
from sql_database_pipeline import sql_database
import humanize 
import logging
import dlt
from stores_unnest import unnest_store
logging.basicConfig(level=logging.INFO)

pipeline = dlt.pipeline(pipeline_name="storess_pipeline")
pipeline.drop()


pipeline = dlt.pipeline(
    pipeline_name="storess_pipeline",
    destination="snowflake",
    dataset_name="unnest_pg_to_sf"
)

pipeline.run(unnest_store())