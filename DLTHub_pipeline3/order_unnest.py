import ast
import dlt
import pandas as pd
from typing import Iterator
import logging
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)

@dlt.resource(columns={
    'order_id': {'data_type': 'bigint'},
    'customer_id': {'data_type': 'text'},
    'order_date': {'data_type': 'date'},
    'status': {'data_type': 'text'},
    'total_amount': {'data_type': 'decimal'},
})
def unnest_order() -> Iterator[pd.DataFrame]:
    source = sql_database().with_resources("orders")
    logging.info("Unnesting orders table")

    for df in source:
        logging.info(f"Processing {len(df)} rows from orders table")

        df['customer'] = df['customer'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else {})
        df['customer_id'] = df['customer'].apply(lambda x: x.get('customer_id') if isinstance(x, dict) else None)
        logging.info("Customer IDs extracted successfully.")
        print(df[['order_id', 'customer_id']].head())
        yield df[['order_id', 'customer_id', 'order_date', 'status', 'total_amount']]

if __name__ == "__main__":
    for df in unnest_order():
        print(df.head(5))
