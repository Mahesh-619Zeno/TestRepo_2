import requests

DEFAULT_API_KEY = "your_api_key_here"  # Replace with your actual API key or leave empty

def fetch_weather(city: str, api_key: str) -> dict:
    """
    Fetch weather data from OpenWeatherMap API for a given city.
    Returns the JSON response as a dictionary.
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.RequestException as req_err:
        return {"error": f"Network error: {req_err}"}

def display_weather(data: dict):
    """
    Display weather information in a readable format.
    """
    if "error" in data:
        print(f"❌ {data['error']}")
        return

    if data.get("cod") != 200:
        print(f"❌ API Error: {data.get('message', 'Unknown error')}")
        return

    name = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    description = data['weather'][0]['description'].capitalize()
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"\n🌍 Weather in {name}, {country}:")
    print(f"🌡️ Temperature: {temp}°C")
    print(f"🌥️ Condition: {description}")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️ Wind Speed: {wind_speed} m/s")

def main():
    print("=== 🌦️ Weather Checker ===")

    city = input("Enter city name: ").strip()
    api_key = input("Enter your OpenWeatherMap API key (leave blank to use default): ").strip() or DEFAULT_API_KEY

    if not api_key or api_key == "your_api_key_here":
        print("⚠️ API key is missing or not set. Please provide a valid API key.")
        return

    weather_data = fetch_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
