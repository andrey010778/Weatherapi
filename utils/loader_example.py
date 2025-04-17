from dotenv import load_dotenv
import os
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'

response = requests.get(API_URL, params={'key': API_KEY, 'q': 'Санкт-Петербург', 'days': DAYS, 'aqi': "YES", 'lang': LANG})
data = response.json()
location = data['location']
forecast_hours = data['forecast']['forecastday'][0]['hour']
city_name = location['name']
current = data['current']
air_quality = current['air_quality']
print(air_quality)