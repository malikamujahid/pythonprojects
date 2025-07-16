import ast
import dlt
import pandas as pd
from typing import Iterator
import logging
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)

@dlt.resource(columns={
    'store_id': {'data_type': 'bigint'},
    'name': {'data_type': 'text'},
    'longitude': {'data_type': 'decimal'},
    'latitude': {'data_type': 'decimal'},
    'city': {'data_type': 'text'},
    'street': {'data_type': 'text'},
    'zipcode': {'data_type': 'text'},
})
def unnest_store() -> Iterator[pd.DataFrame]:
    source = sql_database().with_resources("stores")
    logging.info("Unnesting stores table")

    for df in source:
        logging.info(f"Processing {len(df)} rows from stores table")
        df['location'] = df['location'].apply(ast.literal_eval)
        df['address'] = df['address'].apply(ast.literal_eval)
        df['longitude'] = df['location'].apply(lambda x: x.get('longitude') if isinstance(x, dict) else None)
        df['latitude'] = df['location'].apply(lambda x: x.get('latitude') if isinstance(x, dict) else None)
        df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)
        df['street'] = df['address'].apply(lambda x: x.get('street') if isinstance(x, dict) else None)
        df['zipcode'] = df['address'].apply(lambda x: x.get('zipcode') if isinstance(x, dict) else None)
        print(df.head())
        print(df.columns)
        logging.info("nested data extracted successfully.")

        yield df[['store_id', 'name', 'longitude', 'latitude', 'city', 'street', 'zipcode']]
        
        logging.info("Dataframe yielded with unnested columns.")

if __name__ == "__main__":
    for df in unnest_store():
        print(df)