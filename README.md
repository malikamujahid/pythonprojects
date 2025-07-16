**DLTHub Pipeliline**
This project sets up a DLTHub pipeline that extracts data from:

ClickUp API (team information)

Snowflake Database (specified table)

Extracted data can be printed or stored in a local DuckDB file.

**DLTHub Pipeline2**

This project implements a data pipeline that transfers data from a PostgreSQL database to a Snowflake data warehouse using the DLT (Data Load Tool) framework. 
It extracts tables from the PostgreSQL source, transforms them into a compatible format, and loads them into a specified Snowflake schema. 
The pipeline is designed to handle dynamic table extraction and ensures efficient, structured data migration between the two systems.

**DLTHub Pipeline 3**
This project contains a collection of Python scripts using the DLTHub (Data Load Tool) framework. It focuses on transferring data from a PostgreSQL database into Snowflake, with custom unnesting applied where needed.
5 Unnesting Scripts:
Extract and flatten nested data from PostgreSQL tables using pandas (e.g., unnesting JSON columns or lists of dictionaries).
5 Pipeline Scripts:
Configure and execute DLTHub pipelines that load the unnested data into dedicated Snowflake schemas and tables.
