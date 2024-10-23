import sqlite3

def init_db():
    conn = sqlite3.connect('workouts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS workouts
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  date TEXT,
                  type TEXT,
                  duration INTEGER)''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
