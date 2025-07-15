import dlt
import requests
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logging.basicConfig(level=logging.INFO) 
@dlt.resource
def clickup_teams():
    header= {"authorization": os.getenv("DLT_SECRETS__value")}
    logging.info("Authorization header set.")

    response= requests.get("https://api.clickup.com/api/v2/team", headers=header)
    logging.info("Starting to fetch team data from ClickUp API...")
    if response.status_code != 200:
        logging.error(f"Failed to fetch team data: {response.status_code} - {response.text}")
    else:
        logging.info("Successfully fetched team data.")

    yield response.json()
        

@dlt.source
def clickup_source():
    return clickup_teams()



"""
source = clickup_source()

for item in source.resources["clickup_teams"]:
    print(item)
"""
