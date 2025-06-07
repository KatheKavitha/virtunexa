from weather import get_weather
from notifier import send_email
from logger import log_operation

def main():
    city = input("Enter the city for weather update: ")
    weather_info = get_weather(city)
    print(weather_info)
    send_email("recipient@example.com", f"Weather Update for {city}", weather_info)
    log_operation(city, weather_info)

if __name__ == "__main__":
    main()