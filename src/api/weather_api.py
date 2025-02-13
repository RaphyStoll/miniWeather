from dotenv import load_dotenv
import os
import requests


def get_meteo(ville, apikey):
    # url de l'api
    url_base = "http://api.openweathermap.org/data/2.5/weather"

    # parametres de la requete
    parametres = {"q": ville, "appid": apikey, "units": "metric"}
    # requete a l'api
    reponse = requests.get(url_base, params=parametres)

    # verifier si la requete a reussi
    if reponse.status_code == 200:
        # analyser la reponse json
        donnees = reponse.json()
        # extraire les donner dans les bonnes variables
        temperature = donnees["main"]["temp"]
        humidite = donnees["main"]["humidity"]
        description = donnees["weather"][0]["description"]
        return {
            "temperature": temperature,
            "humidite": humidite,
            "description": description,
        }
    elif reponse.status_code == 429:
        print("Vous avez dépassé la limite de requêtes autorisée")
        return None
    else:
        print("Erreur lors de la récupération des données météo")
        return None
