import sqlite3

def log_operation(command, response):
    conn = sqlite3.connect("assistant_log.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT,
            response TEXT
        )
    ''')
    cursor.execute('INSERT INTO logs (command, response) VALUES (?, ?)', (command, response))
    conn.commit()
    conn.close()