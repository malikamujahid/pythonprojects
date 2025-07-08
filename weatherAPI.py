import requests
import json
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Starting the weather app")
cityname = input("Which city's weather update do you require? ")
apikey= '011a59f37217cc43b7603707beaf3e17'

try:
    url = f"https://api.openweathermap.org/data/2.5/weather?q={cityname}&appid={apikey}&units=metric"
    response = requests.get(url)
    logging.info("received hhtp response successfully")

except requests.exceptions.HTTPError as httperr:
    logging.error(f"HTTP error occurred: {httperr}")

cityWeather= response.json()

@staticmethod
def descriptionWeather(cityWeather, cityname):
    temp = cityWeather["main"]["temp"]
    humidity = cityWeather["main"]["humidity"]
    description = cityWeather["weather"][0]["description"] 

    print(f"The temperature in {cityname} is {temp}°C\n"
          f"The humidity in {cityname} is {humidity}%\n"
          f"Weather description: {description}")
    logging.info("weather data dispolayedd")

descriptionWeather(cityWeather, cityname )



