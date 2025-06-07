import sqlite3

def log_operation(city, weather_info):
    conn = sqlite3.connect("weather_log.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city TEXT,
            weather TEXT
        )
    ''')
    cursor.execute('INSERT INTO logs (city, weather) VALUES (?, ?)', (city, weather_info))
    conn.commit()
    conn.close()