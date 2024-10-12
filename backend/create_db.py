import sqlite3

def create_database():
    conn = sqlite3.connect('store.db')
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.close()
if __name__ == "__name__":
    create_database()