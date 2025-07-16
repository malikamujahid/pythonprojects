import dlt 
from sql_database_pipeline import sql_database
import humanize 
import logging
import dlt
from employee_unnest import unnest_employees
logging.basicConfig(level=logging.INFO)


pipeline = dlt.pipeline(
    pipeline_name="employee_pipeline",
    destination="snowflake",
    dataset_name="unnest_pg_to_sf"
)

pipeline.run(unnest_employees())