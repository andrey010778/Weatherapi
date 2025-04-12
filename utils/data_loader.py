from dotenv import load_dotenv
import os
import requests


load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DAYS = 1
LANG = 'ru'

def load_data(city):
    
        response = requests.get(API_URL, params={'key': API_KEY, 'q': city, 'days': DAYS, 'lang': LANG})
        data = response.json()

        location = data['location']
        forecast_hours = data['forecast']['forecastday'][0]['hour']
        city_name = location['name']
        current = data['current']
        icon = current['condition']['icon']
        condition = current['condition']['text']
        temp = current['temp_c']
        hours = [h['time'][-5:] for h in forecast_hours]
        temps = [h['temp_c'] for h in forecast_hours]
        ap = [h['pressure_mb'] for h in forecast_hours]
        humidity = [h['humidity'] for h in forecast_hours]
        wind = [h['wind_kph'] for h in forecast_hours]
        wind_dirs = [h['wind_degree'] for h in forecast_hours]
        return {"location": location,
                 "city_name": city_name,
                 "icon": icon,
                 "temp": temp,
                 "hours": hours,
                 "temps": temps,
                 "ap": ap,
                 "humidity": humidity,
                 "wind": wind,
                 "wind_dirs": wind_dirs,
                 "condition": condition}
        