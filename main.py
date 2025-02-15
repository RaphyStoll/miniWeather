# api/weather_api.py
from dotenv import load_dotenv
from src.ui.weather_display import fetch_weather
import os

# from src.test.test_weather_api import test_get


def main():
    api_key = os.getenv("API_KEY")
    if not api_key:
        print("API_KEY not found in .env file")
        return


# test_get(api_key)


if __name__ == "__main__":
    load_dotenv()
    main()
