import tkinter as tk
from weather import get_weather

def show_weather():
    city = entry.get()
    weather_info = get_weather(city)
    result_label.config(text=weather_info)

root = tk.Tk()
root.title("Weather App")

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Get Weather", command=show_weather)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()