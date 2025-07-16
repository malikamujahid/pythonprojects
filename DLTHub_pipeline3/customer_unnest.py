import ast
import dlt
import pandas as pd
from typing import Iterator
import logging
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)

@dlt.resource(columns={
    'customer_id': {'data_type': 'bigint'},
    'name': {'data_type': 'text'},
    'email': {'data_type': 'text'},
    'phone': {'data_type': 'text'},
    'city': {'data_type': 'text'},
    'street': {'data_type': 'text'},
    'zipcode': {'data_type': 'text'},
    'newsletter': {'data_type': 'text'},
    'contact_method': {'data_type': 'text'}
})
def unnest_customers() -> Iterator[pd.DataFrame]:
    source = sql_database().with_resources("customers")
    logging.info("Unnesting customers table")

    for df in source:
        logging.info(f"Processing {len(df)} rows from customers table")
        
        df['address'] = df['address'].apply(ast.literal_eval)
        df['preferences'] = df['preferences'].apply(ast.literal_eval)
        df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)
        df['street'] = df['address'].apply(lambda x: x.get('street') if isinstance(x, dict) else None)
        df['zipcode'] = df['address'].apply(lambda x: x.get('zipcode') if isinstance(x, dict) else None)
        df['newsletter'] = df['preferences'].apply(lambda x: x.get('newsletter') if isinstance(x, dict) else None)
        df['contact_method'] = df['preferences'].apply(lambda x: x.get('contact_method') if isinstance(x, dict) else None)
        print(df.head())
        logging.info("Profile data extracted successfully.")

        yield df[['customer_id', 'name', 'email', 'phone', 'city', 'street', 'zipcode', 'newsletter', 'contact_method']]
        logging.info("Dataframe yielded with unnested columns.")

    


if __name__ == "__main__":
    for df in unnest_customers():
        print(df)


