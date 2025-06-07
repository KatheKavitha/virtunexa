from datetime import datetime
from weather import get_weather
from calculator import calculate

def handle_command(command):
    if "remind me" in command.lower():
        return set_reminder(command)
    elif "weather" in command.lower():
        city = command.split("in")[-1].strip()
        return get_weather(city)
    elif any(op in command for op in "+-*/"):
        return calculate(command)
    else:
        return "Sorry, I didn't understand that command."

def set_reminder(command):
    with open("reminders.txt", "a") as f:
        f.write(command + "\n")
    return "Reminder set!"