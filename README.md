**DLTHub Pipeliline**
This project sets up a DLTHub pipeline that extracts data from:

ClickUp API (team information)

Snowflake Database (specified table)

Extracted data can be printed or stored in a local DuckDB file.

**DLTHub Pipeline2**

This project implements a data pipeline that transfers data from a PostgreSQL database to a Snowflake data warehouse using the DLT (Data Load Tool) framework. 
It extracts tables from the PostgreSQL source, transforms them into a compatible format, and loads them into a specified Snowflake schema. 
The pipeline is designed to handle dynamic table extraction and ensures efficient, structured data migration between the two systems.
