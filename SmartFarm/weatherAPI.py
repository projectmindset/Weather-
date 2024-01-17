#weather app
import requests
import datetime
import time

def collect_weather_information():
    api_key = 'a6445b5e6e4b693b38f8de51f435a8e4'
    user_input = input('Enter City: ')

    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

    # print(weather_data.json())
    weather = weather_data.json()['weather'][0]['description']
    temp = weather_data.json()['main']['feels_like']

    print(" ")
    print("Fetching weather data..... ")
    print(" ")
    time.sleep(3)
    print(weather)
    time.sleep(2)

    print(temp)
