import pandas as pd
import ast 
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas 
import logging
import os

logging.basicConfig(level=logging.INFO)


conn = snowflake.connector.connect(
    user= os.getenv('user'), 
    password=os.getenv('password'),
    account=os.getenv('account'),  
    warehouse=os.getenv('warehouse'),
    database=os.getenv('database'),
    schema=os.getenv('schema')) 

cursor = conn.cursor()
logging.info("Connection established successfully with snowflake.")
cursor.execute("SELECT CURRENT_USER(), CURRENT_REGION();")
print(cursor.fetchall())


df= pd.read_csv('users_with_sub.csv')
logging.info("CSV file loaded successfully.")

# Convert the 'profile' column from string representation of dictionaries to actual dictionaries
df['profile'] = df['profile'].apply(ast.literal_eval)

# Convert the 'subscriptions' column from string representation of lists to actual lists
df['subscriptions'] = df['subscriptions'].apply(ast.literal_eval)

df['age']= df['profile'].apply(lambda x: x.get('age', None))
df['gender']= df['profile'].apply(lambda x: x.get('gender', None))
df['street'] = df['profile'].apply(lambda x: x.get('address', {}).get('street'))
df['city'] = df['profile'].apply(lambda x: x.get('address', {}).get('city'))
df['zipcode'] = df['profile'].apply(lambda x: x.get('address', {}).get('zipcode'))
logging.info("Profile data extracted successfully.")


df_exploded = df.explode('subscriptions')

df_exploded['plan'] = df_exploded['subscriptions'].apply(lambda x: x.get('plan'))
df_exploded['start_date'] = df_exploded['subscriptions'].apply(lambda x: x.get('start_date'))
df_exploded['active'] = df_exploded['subscriptions'].apply(lambda x: x.get('active'))
df_exploded['start_date'] = pd.to_datetime(df_exploded['start_date'])
logging.info("Subscriptions data exploded and extracted successfully.")

df_exploded = df_exploded.drop(columns=['profile', 'subscriptions'])
df_exploded.columns = [col.lower() for col in df_exploded.columns]
df_exploded = df_exploded.reset_index(drop=True)


df_exploded.to_csv('exploded.csv', index=False)
logging.info("Exploded DataFrame saved to CSV successfully.") 

# Upload DataFrame to Snowflake
success, nchunks, nrows, _ = write_pandas(
    conn=conn,
    df=df_exploded,
    table_name= os.getenv('table_name'),  # Table must already exist
    database=os.getenv('database'),
    schema=os.getenv('schema'),
    overwrite=True  # Set to True to overwrite the table
)
logging.info(f"Data uploaded to Snowflake successfully: {success}, Number of chunks: {nchunks}, Number of rows: {nrows}")











    