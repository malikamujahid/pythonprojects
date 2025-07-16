import dlt
from dlt.sources.sql_database import sql_database
import humanize
import logging

def load_entire_database() -> None:
    """Use the sql_database source to completely load all tables in a database"""
    pipeline = dlt.pipeline(pipeline_name="postgrestosnowflake", destination='snowflake', dataset_name="postgres_to_snowflake_all_tables")

    # By default the sql_database source reflects all tables in the schema
    # The database credentials are sourced from the `.dlt/secrets.toml` configuration
    source = sql_database()

    # Run the pipeline. For a large db this may take a while
    info = pipeline.run(source, write_disposition="replace")
    print(info)

if __name__ == "__main__":
    # Load the entire database
    load_entire_database()

    # Print the summary of the pipeline run
    logging.info("Pipeline run completed.")