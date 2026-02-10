import requests, json
import sys

api_key = "3bfcdbea2ddd48d8ad0173610261002"
BASE_URL = "https://api.weatherapi.com"

def get_weather(city_name):
   # Parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" # Get temperature in Celsius by default
    }

    try:
        # Make the HTTP GET request
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)

        # Convert response to a Python dictionary
        data = response.json()

        if data.get("cod") != 200:
            print(f"Error from API: {data.get('message', 'Unknown error')}")
            return None

        return data

    except requests.exceptions.RequestException as e:
        print(f"Network or request error: {e}")
        return None
    
def display_weather(data):
    if data:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        desc = data['weather'][0]['description'].capitalize()
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        print(f"\n--- Weather in {city}, {country} ---")
        print(f"Condition  : {desc}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity   : {humidity}%")
        print(f"Wind Speed : {wind_speed} m/s")
        print("-" * (len(city) + len(country) + 19))
    else:
        print("Could not retrieve weather data.")

def main():
    city_name = input("Enter city name: ").strip()
    if not city_name:
        print("City name cannot be empty.")
        sys.exit(1)

    weather_data = get_weather(city_name)
    display_weather(weather_data)

if __name__ == "__main__":
    main()