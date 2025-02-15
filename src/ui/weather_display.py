import tkinter as tk
from tkinter import ttk, messagebox
from src.api.weather_api import get_current_weather, get_forecast
from src.cache.cache_manager import CacheManager
from dotenv import load_dotenv
import os

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

# Initialiser le gestionnaire de cache
cache_manager = CacheManager(expiration_time=900)  # 15 minutes


def format_weather_info(weather_info):
    return (
        f"Température: {weather_info['temperature']}°C\n"
        f"Humidité: {weather_info['humidity']}%\n"
        f"Description: {weather_info['description']}"
    )


def format_forecast_info(forecast_info):
    formatted_forecast = {}
    for entry in forecast_info:
        date_str = entry["date"].strftime("%Y-%m-%d")
        if date_str not in formatted_forecast:
            formatted_forecast[date_str] = []
        formatted_forecast[date_str].append(
            (
                entry["date"].strftime("%H:%M"),
                entry["temperature"],
                entry["description"],
            )
        )
    return formatted_forecast


def fetch_weather():
    city = entry_city.get()
    api_key = os.getenv("API_KEY")

    if not api_key:
        messagebox.showerror("Erreur", "Clé API non trouvée.")
        return

    try:
        weather_info, forecast_info = cache_manager.get(
            city, get_weather_data, city, api_key
        )

        # Mettre à jour le label avec les informations météorologiques actuelles
        label_weather.config(
            text=f"Météo actuelle:\n{format_weather_info(weather_info)}"
        )

        # Mettre à jour les prévisions
        update_forecast_display(format_forecast_info(forecast_info))
    except Exception as e:
        messagebox.showerror(
            "Erreur", f"Erreur lors de la récupération des données météo: {e}"
        )


def get_weather_data(city, api_key):
    # Simuler la récupération de données depuis une source externe
    weather_info = get_current_weather(city, api_key)
    forecast_info = get_forecast(city, api_key)
    return weather_info, forecast_info


def update_forecast_display(forecast_info):
    # Effacer les widgets existants dans la zone de prévision
    for widget in forecast_frame.winfo_children():
        widget.destroy()

    # Créer des colonnes pour chaque jour de prévision
    col = 0
    for date, forecasts in forecast_info.items():
        # Ajouter un séparateur vertical avant chaque nouvelle date (sauf pour la première)
        if col != 0:
            ttk.Separator(forecast_frame, orient="vertical").grid(
                row=0, column=col, rowspan=len(forecasts) + 2, sticky="ns", padx=10
            )

        ttk.Label(forecast_frame, text=date, style="Heading.TLabel").grid(
            row=0, column=col, padx=5, pady=5
        )
        ttk.Label(forecast_frame, text="Heure", style="Subheading.TLabel").grid(
            row=1, column=col, padx=5, pady=2
        )
        ttk.Label(forecast_frame, text="Temp (°C)", style="Subheading.TLabel").grid(
            row=1, column=col + 1, padx=5, pady=2
        )
        ttk.Label(forecast_frame, text="Description", style="Subheading.TLabel").grid(
            row=1, column=col + 2, padx=5, pady=2
        )

        for i, (hour, temp, desc) in enumerate(forecasts):
            ttk.Label(forecast_frame, text=hour, style="TLabel").grid(
                row=i + 2, column=col, padx=5, pady=2
            )
            ttk.Label(forecast_frame, text=f"{temp}°C", style="TLabel").grid(
                row=i + 2, column=col + 1, padx=5, pady=2
            )
            ttk.Label(forecast_frame, text=desc, style="TLabel").grid(
                row=i + 2, column=col + 2, padx=5, pady=2
            )

        col += 3  # Passer à la colonne suivante pour le prochain jour


# Initialisation de l'interface Tkinter avec style
root = tk.Tk()
root.title("Weather App")

# Appliquer un style
style = ttk.Style()
style.configure(
    "TButton",
    font=("Helvetica", 12),
    padding=6,
    relief="flat",
    background="#4CAF50",
    foreground="white",
)
style.configure("TLabel", font=("Helvetica", 12), padding=5)
style.configure("Heading.TLabel", font=("Helvetica", 12, "bold"), padding=5)
style.configure("Subheading.TLabel", font=("Helvetica", 12, "italic"), padding=5)
style.configure("WeatherBox.TFrame", borderwidth=2, relief="groove")

# Créer les widgets avec style
ttk.Label(root, text="Entrez le nom de la ville:", style="TLabel").pack(pady=10)
entry_city = ttk.Entry(root, font=("Helvetica", 12))
entry_city.pack(pady=10)

button_fetch = ttk.Button(
    root, text="Obtenir la météo", command=fetch_weather, style="TButton"
)
button_fetch.pack(pady=20)

# Frame pour encadrer les informations météorologiques actuelles
weather_box = ttk.Frame(root, style="WeatherBox.TFrame")
weather_box.pack(pady=10, padx=10, fill="none", expand=False)

label_weather = ttk.Label(weather_box, text="Météo actuelle: None", style="TLabel")
label_weather.pack(pady=10)

# Frame pour afficher les prévisions
forecast_frame = ttk.Frame(root)
forecast_frame.pack(pady=10)

root.mainloop()
