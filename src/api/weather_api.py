import os
import requests
import time
from dotenv import load_dotenv
from datetime import datetime


def get_current_weather(city, apikey):
    # url de l'api
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    # parametres de la requete
    params = {"q": city, "appid": apikey, "units": "metric"}
    # requete a l'api
    response = requests.get(base_url, params=params)

    # verifier si la requete a reussi
    if response.status_code == 200:
        # analyser la reponse json
        data = response.json()
        # extraire les donner dans les bonnes variables
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]
        return {
            "temperature": temperature,
            "humidity": humidity,
            "description": description,
        }
    elif response.status_code == 429:
        print("API key limit exceeded")
        return None
    else:
        print("Error retrieving weather data")
        return None


def get_forecast(city, api_key):
    # URL de l'API
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    # Paramètres de la requête
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "cnt": 72,
    }  # nbr d'heures de prévisions

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        forecasts = []

        # Extraire les données de la réponse
        for forecast_item in data["list"]:
            date = datetime.fromtimestamp(forecast_item["dt"])
            temperature = forecast_item["main"]["temp"]
            description = forecast_item["weather"][0]["description"]
            forecasts.append(
                {"date": date, "temperature": temperature, "description": description}
            )
        return forecasts
    elif response.status_code == 429:
        print("API key limit exceeded")
        return None
    else:
        print(f"Error {response.status_code} occurred while fetching weather data")
        return None
