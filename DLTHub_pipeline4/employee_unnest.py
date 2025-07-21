import ast
import dlt
import pandas as pd
from typing import Iterator
import logging
from dlt.sources.sql_database import sql_database

logging.basicConfig(level=logging.INFO)

@dlt.resource(columns={
    'employee_id': {'data_type': 'bigint'},
    'name': {'data_type': 'text'},
    'email': {'data_type': 'text'},
    'phone': {'data_type': 'text'},
    'city': {'data_type': 'text'},
    'street': {'data_type': 'text'},
    'zipcode': {'data_type': 'text'},
    'position': {'data_type': 'text'},
    'joined_date': {'data_type': 'date'},
})
def unnest_employees() -> Iterator[pd.DataFrame]:
    source = sql_database().with_resources("employees")
    logging.info("Unnesting employees table")

    for df in source:
        logging.info(f"Processing {len(df)} rows from employees table")
        
        df['contact'] = df['contact'].apply(ast.literal_eval)
        df['address'] = df['address'].apply(ast.literal_eval)
        df['city'] = df['address'].apply(lambda x: x.get('city') if isinstance(x, dict) else None)
        df['street'] = df['address'].apply(lambda x: x.get('street') if isinstance(x, dict) else None)
        df['zipcode'] = df['address'].apply(lambda x: x.get('zipcode') if isinstance(x, dict) else None)
        df['email'] = df['contact'].apply(lambda x: x.get('email') if isinstance(x, dict) else None)
        df['phone'] = df['contact'].apply(lambda x: x.get('phone') if isinstance(x, dict) else None)
        print(df.head())
        logging.info("nested data extracted successfully.")

        yield df[['employee_id', 'name', 'email', 'phone', 'city', 'street', 'zipcode', 'position', 'joined_date']]
        logging.info("Dataframe yielded with unnested columns.")

    

'''
if __name__ == "__main__":
    for df in unnest_employees():
        print(df)
        '''