import requests
from dataclasses import dataclass


api_key = "766443a8a1db73992dc192eabba6b5d8"

@dataclass
class WeatherData:
    main : str
    description : str
    icon: str
    temperature : float


city = input("city name: ")

def main(city, api_key):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}").json()
    data = WeatherData(
        main = weather_data.get('weather')[0]['main'],
        description=weather_data.get('weather')[0]['description'],
        icon=weather_data.get('weather')[0]['icon'],
        temperature=float(weather_data.get('main')['temp'])
    )
    return data



