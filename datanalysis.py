import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_data(filename):
    logging.info("Loading data")
    
    df = pd.read_csv(filename) 
    print(df.head)

    logging.info("Data loaded successfully")

    # Handle nulls
    logging.info("Setting null values")
    df.fillna({
        'Certificate': 'Not Rated',
        'Meta_score': 0,
        'Gross': '0', 
    }, inplace=True)

    logging.info("Null values set successfully")
    logging.info("Redefining data types")

    # Redefine data type
    df['Gross'] = df['Gross'].str.replace(',', '').astype(int)
    logging.info("Data types redefined successfully")
    return df

clean_data('movies.csv')