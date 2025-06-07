import requests

API_KEY = "YOUR_API_KEY_HERE"  # Replace this with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'wind_speed': data['wind']['speed']
            }
            return weather
        else:
            print("Error:", data.get("message", "Unknown error occurred."))
    except requests.RequestException as e:
        print("Network error:", e)

def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")

if __name__ == "__main__":
    main()
