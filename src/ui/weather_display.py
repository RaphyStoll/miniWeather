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

# Charger les favoris depuis un fichier
favorites_file = "../data/favorites.json"
if os.path.exists(favorites_file):
    with open(favorites_file, "r") as file:
        favorites = json.load(file)
else:
    favorites = []

# Limite de favoris
FAVORITE_LIMIT = 10

# Charger les villes rapides depuis un fichier
quick_cities_file = "quick_cities.json"
if os.path.exists(quick_cities_file):
    with open(quick_cities_file, "r") as file:
        quick_cities = json.load(file)
else:
    quick_cities = []


def save_favorites():
    with open(favorites_file, "w") as file:
        json.dump(favorites, file)


def save_quick_cities():
    with open(quick_cities_file, "w") as file:
        json.dump(quick_cities, file)


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


def fetch_weather(event=None):
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


def add_favorite():
    city = entry_city.get()
    if city not in favorites:
        if FAVORITE_LIMIT != -1 and len(favorites) >= FAVORITE_LIMIT:
            messagebox.showinfo("Info", "Limite de favoris atteinte.")
            return
        favorites.append(city)
        save_favorites()
        update_favorites_display()
    else:
        messagebox.showinfo("Info", "Cette ville est déjà dans vos favoris.")


def remove_favorite(city):
    if city in favorites:
        favorites.remove(city)
        save_favorites()
        update_favorites_display()


def update_favorites_display():
    # Effacer les widgets existants dans la zone des favoris
    for widget in favorites_frame.winfo_children():
        widget.destroy()

    # Créer des boutons pour chaque ville favorite
    for city in favorites:
        btn = ttk.Button(
            favorites_frame,
            text=city,
            command=lambda c=city: fetch_weather_for_favorite(c),
        )
        btn.pack(side="left", padx=5, pady=5)
        btn_remove = ttk.Button(
            favorites_frame, text="✖", command=lambda c=city: remove_favorite(c)
        )
        btn_remove.pack(side="left", padx=2, pady=5)


def fetch_weather_for_favorite(city):
    entry_city.delete(0, tk.END)
    entry_city.insert(0, city)
    fetch_weather()


def show_favorites():
    # Afficher la liste des favoris
    favorites_window = tk.Toplevel(root)
    favorites_window.title("Villes Favorites")

    favorites_list_frame = ttk.Frame(favorites_window)
    favorites_list_frame.pack(pady=10)

    for city in favorites:
        btn = ttk.Button(
            favorites_list_frame,
            text=city,
            command=lambda c=city: fetch_weather_for_favorite(c),
        )
        btn.pack(side="left", padx=5, pady=5)
        btn_remove = ttk.Button(
            favorites_list_frame, text="✖", command=lambda c=city: remove_favorite(c)
        )
        btn_remove.pack(side="left", padx=2, pady=5)


def add_quick_city():
    city = entry_city.get()
    if city not in quick_cities:
        quick_cities.append(city)
        save_quick_cities()
        update_quick_cities_display()
    else:
        messagebox.showinfo("Info", "Cette ville est déjà dans vos villes rapides.")


def remove_quick_city(city):
    if city in quick_cities:
        quick_cities.remove(city)
        save_quick_cities()
        update_quick_cities_display()


def update_quick_cities_display():
    # Effacer les widgets existants dans la zone des villes rapides
    for widget in quick_cities_frame.winfo_children():
        widget.destroy()

    # Créer des boutons pour chaque ville rapide
    for city in quick_cities:
        btn = ttk.Button(
            quick_cities_frame,
            text=city,
            command=lambda c=city: fetch_weather_for_quick_city(c),
        )
        btn.pack(side="left", padx=5, pady=5)
        btn_remove = ttk.Button(
            quick_cities_frame, text="✖", command=lambda c=city: remove_quick_city(c)
        )
        btn_remove.pack(side="left", padx=2, pady=5)


def fetch_weather_for_quick_city(city):
    entry_city.delete(0, tk.END)
    entry_city.insert(0, city)
    fetch_weather()


def show_quick_cities():
    # Afficher la liste des villes rapides
    quick_cities_window = tk.Toplevel(root)
    quick_cities_window.title("Villes Rapides")

    quick_cities_list_frame = ttk.Frame(quick_cities_window)
    quick_cities_list_frame.pack(pady=10)

    for city in quick_cities:
        btn = ttk.Button(
            quick_cities_list_frame,
            text=city,
            command=lambda c=city: fetch_weather_for_quick_city(c),
        )
        btn.pack(side="left", padx=5, pady=5)
        btn_remove = ttk.Button(
            quick_cities_list_frame,
            text="✖",
            command=lambda c=city: remove_quick_city(c),
        )
        btn_remove.pack(side="left", padx=2, pady=5)


def on_escape(event):
    root.quit()


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
entry_city.bind(
    "<Return>", fetch_weather
)  # Lier la touche Enter pour valider la recherche

button_fetch = ttk.Button(
    root, text="Obtenir la météo", command=fetch_weather, style="TButton"
)
button_fetch.pack(pady=20)

# Bouton étoile pour ajouter aux favoris
star_button = ttk.Button(root, text="⭐", command=add_favorite, style="TButton")
star_button.pack(side="left", padx=5, pady=10)

# Bouton pour accéder à la liste des favoris
favorites_button = ttk.Button(
    root, text="Favoris", command=show_favorites, style="TButton"
)
favorites_button.pack(side="left", padx=5, pady=10)

# Bouton pour ajouter une ville rapide
quick_city_button = ttk.Button(
    root, text="➕ Ville Rapide", command=add_quick_city, style="TButton"
)
quick_city_button.pack(side="left", padx=5, pady=10)

# Bouton pour accéder à la liste des villes rapides
quick_cities_button = ttk.Button(
    root, text="Villes Rapides", command=show_quick_cities, style="TButton"
)
quick_cities_button.pack(side="left", padx=5, pady=10)

# Frame pour encadrer les informations météorologiques actuelles
weather_box = ttk.Frame(root, style="WeatherBox.TFrame")
weather_box.pack(pady=10, padx=10, fill="none", expand=False)

label_weather = ttk.Label(weather_box, text="Météo actuelle: None", style="TLabel")
label_weather.pack(pady=10)

# Frame pour afficher les prévisions
forecast_frame = ttk.Frame(root)
forecast_frame.pack(pady=10)

# Frame pour afficher les favoris
favorites_frame = ttk.Frame(root)
favorites_frame.pack(pady=10)

# Frame pour afficher les villes rapides
quick_cities_frame = ttk.Frame(root)
quick_cities_frame.pack(pady=10)

# Mettre à jour l'affichage des favoris
update_favorites_display()

# Mettre à jour l'affichage des villes rapides
update_quick_cities_display()

# Lier la touche Esc pour quitter l'application
root.bind("<Escape>", on_escape)

root.mainloop()
