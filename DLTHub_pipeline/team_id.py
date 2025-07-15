import requests
import os 
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)
api_key = os.getenv("DLT_SECRETS__value")
logging.info(f"Authorization header value: {api_key!r}") 

logging.info("Starting to fetch team data from ClickUp API..." )
headers = {"Authorization": os.getenv("DLT_SECRETS__value")}
logging.info("Authorization header set.")

r = requests.get("https://api.clickup.com/api/v2/team", headers=headers)
if r.status_code != 200:
    logging.error(f"Failed to fetch team data: {r.status_code} - {r.text}")
else:
    logging.info("Successfully fetched team data.")
    
print(r.json())

