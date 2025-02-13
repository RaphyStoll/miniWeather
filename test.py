import requests


def obtenir_meteo(ville, api_key):
    # URL de base pour l'API météo
    url_base = "http://api.openweathermap.org/data/2.5/weather"

    # Paramètres de la requête
    parametres = {
        "q": ville,
        "appid": api_key,
        "units": "metric",  # Utiliser des unités métriques pour la température
    }

    # Envoyer la requête GET à l'API
    reponse = requests.get(url_base, params=parametres)

    # Vérifier si la requête a réussi
    if reponse.status_code == 200:
        # Analyser la réponse JSON
        donnees = reponse.json()

        # Extraire les informations nécessaires
        temperature = donnees["main"]["temp"]
        humidite = donnees["main"]["humidity"]
        description = donnees["weather"][0]["description"]

        # Retourner les informations sous forme de dictionnaire
        return {
            "temperature": temperature,
            "humidite": humidite,
            "description": description,
        }
    else:
        # En cas d'erreur, retourner un message d'erreur
        print("Erreur lors de la récupération des données météo")
        return None


def main():
    # Remplacez par votre clé API OpenWeatherMap
    api_key = "495d7314b4a70dc88270996698576dad"

    # Demander à l'utilisateur d'entrer le nom de la ville
    ville = input("Entrez le nom de la ville : ")

    # Obtenir les données météo
    meteo = obtenir_meteo(ville, api_key)

    # Afficher les résultats
    if meteo:
        print(f"Température à {ville}: {meteo['temperature']}°C")
        print(f"Humidité: {meteo['humidite']}%")
        print(f"Conditions: {meteo['description']}")
    else:
        print("Impossible de récupérer les données météo pour cette ville.")


if __name__ == "__main__":
    main()
