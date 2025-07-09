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

def recommend(genre, ratingpref):
    logging.info("Recommending movies")
        
    df = pd.read_csv('movies.csv')
    filtered_df = df[(df['Genre'] == genre) | (df['IMDB_Rating'] >= ratingpref)]
        
    if filtered_df.empty:
        logging.warning("No movies found for the given criteria")
        return "No recommendations available"   
        
    else:
        print(filtered_df.head())

        
clean_data('movies.csv')
user_input= input("Enter the genre and  rating preference: eg (action, 8.5): ")
genre, ratingpref = user_input.split(',')
genre = genre.strip()
ratingpref = float(ratingpref.strip()) 
        
print("Recommended Movies:")
recommendations = recommend(genre, ratingpref)
print(recommendations)
    
    