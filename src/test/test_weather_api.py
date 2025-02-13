from src.api.weather_api import get_meteo


def test_get(api_key):
    ville = input("Entrez le nom de la ville : ")
    meteo = get_meteo(ville, api_key)
    if meteo:
        print(f"Température à {ville}: {meteo['temperature']}°C")
        print(f"Humidité: {meteo['humidite']}%")
        print(f"Conditions: {meteo['description']}")
    else:
        print("Impossible de récupérer les données météo pour cette ville.")
