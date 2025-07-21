import json
import pandas as pd
import logging

def load_data(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
        #wrap dictionary into list
        if isinstance(data, dict):
            data = [data]  
        return pd.DataFrame(data)
    
df = load_data("nested_json.json")


df['user_id'] = df['user'].apply(lambda x: x.get('id'))
df['user_name_first'] = df['user'].apply(lambda x: x.get('name', {}).get('first'))
df['user_name_last'] = df['user'].apply(lambda x: x.get('name', {}).get('last'))
df['location_country'] = df['user'].apply(lambda x: x.get('location', {}).get('country'))
df['location_city_name'] = df['user'].apply(lambda x: x.get('location', {}).get('city', {}).get('name'))
df['postal_code'] = df['user'].apply(lambda x: x.get('location', {}).get('city', {}).get('postal', {}).get('code'))
df['postal_area'] = df['user'].apply(lambda x: x.get('location', {}).get('city', {}).get('postal', {}).get('area'))

df['account_created_at'] = df['account'].apply(lambda x: x.get('created_at'))
df['account_status'] = df['account'].apply(lambda x: x.get('status'))

print(df[['user_id', 'user_name_first', 'user_name_last',
          'location_country', 'location_city_name', 'postal_code',
          'postal_area', 'account_created_at', 'account_status']])
