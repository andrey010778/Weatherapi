from dotenv import load_dotenv
import os
import requests


load_dotenv()

API_KEY = 'ace812db805f4d4a8fd230715252304'
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'



response = requests.get(API_URL, params={'key': API_KEY, 'q': 'Санкт-Петербург', 'days': DAYS, 'aqi': "yes", 'lang': LANG})
data = response.json()

location = data['location']
forecast_hours = data['forecast']['forecastday'][0]['hour']
city_name = location['name']
current = data['current']
air_quality = current['air_quality']
print(air_quality)

location = data['location']
forecast_hours = data['forecast']['forecastday'][0]['hour']
city_name = location['name']
current = data['current']
icon = current['condition']['icon']
condition = current['condition']['text']
temp = current['temp_c']
air_quality = current['air_quality']
co_now = air_quality['co']
no2_now = air_quality['no2']
o3_now = air_quality['o3']
so2_now = air_quality['so2']
pm2_5_now = air_quality['pm2_5']
pm10_now = air_quality['pm10']
hours = [h['time'][-5:] for h in forecast_hours]
    # temps = [h['temp_c'] for h in forecast_hours]
    # ap = [h['pressure_mb'] for h in forecast_hours]
    # humidity = [h['humidity'] for h in forecast_hours]
    # wind = [h['wind_kph'] for h in forecast_hours]
    # wind_dirs = [h['wind_degree'] for h in forecast_hours]
co = [h['air_quality']['co'] for h in forecast_hours] 
no2 = [h['air_quality']['no2'] for h in forecast_hours]
o3 = [h['air_quality']['o3'] for h in forecast_hours]
so2 = [h['air_quality']['so2'] for h in forecast_hours]
pm2_5 = [h['air_quality']['pm2_5'] for h in forecast_hours]
pm10 = [h['air_quality']['pm10'] for h in forecast_hours]

print(co, no2, o3, so2, pm2_5, pm10)