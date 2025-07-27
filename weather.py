from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()
def get_current_weather(city="Bengaluru"):
    request_url = f"https://api.weatherstack.com/current?access_key={os.getenv("API_KEY")}&query={city}"
    weather_data = requests.get(request_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nEnter the city name: ")

    #Check for empty strings or string with only spaces
    if not bool(city.strip()):
        city = "Bengaluru"
    
    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)