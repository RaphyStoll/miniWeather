from src.api.weather_api import get_current_weather, get_forecast


def test_get(api_key):
    choise = input(
        "Entrez '1' pour la météo actuelle et '2' pour les prévisions météo : "
    )
    if choise == "1":
        test_base(api_key)
    elif choise == "2":
        test_forecast(api_key)
    else:
        print("Choix invalide.")


def test_base(api_key):
    ville = input("Entrez le nom de la ville : ")
    meteo = get_current_weather(ville, api_key)
    if meteo:
        print(f"Température à {ville}: {meteo['temperature']}°C")
        print(f"Humidité: {meteo['humidity']}%")
        print(f"Conditions: {meteo['description']}")
    else:
        print("Impossible de récupérer les données météo pour cette ville.")


def test_forecast(api_key):
    ville = input("Entrez le nom de la ville : ")
    forecast = get_forecast(ville, api_key)
    if forecast:
        for day in forecast:
            print(f"Date: {day['date']}")
            print(f"Température: {day['temperature']}°C")
            print(f"Conditions: {day['description']}")
            print("-" * 20)
    else:
        print("Impossible de récupérer les prévisions météo pour cette ville.")
