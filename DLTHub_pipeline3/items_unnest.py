import ast
import dlt
import pandas as pd
from typing import Iterator
import logging
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)

@dlt.resource(columns={
    'item_id': {'data_type': 'bigint'},
    'name': {'data_type': 'text'},
    'category': {'data_type': 'text'},
    'price': {'data_type': 'decimal'},
    'brand': {'data_type': 'text'},
    'warranty_years': {'data_type': 'bigint'}, 
})
def unnest_items() -> Iterator[pd.DataFrame]:
    source = sql_database().with_resources("items")
    logging.info("Unnesting items table")

    for df in source:
        logging.info(f"Processing {len(df)} rows from items table")
        
        df['metadata'] = df['metadata'].apply(ast.literal_eval)
        
        df['brand'] = df['metadata'].apply(lambda x: x.get('brand') if isinstance(x, dict) else None)
        df['warranty_years'] = df['metadata'].apply(lambda x: x.get('warranty_years') if isinstance(x, dict) else None)
        print(df.head())
        logging.info("nested data extracted successfully.")

        yield df[['item_id', 'name', 'category', 'price', 'brand', 'warranty_years']]
        logging.info("Dataframe yielded with unnested columns.")

if __name__ == "__main__":
    for df in unnest_items():
        print(df)