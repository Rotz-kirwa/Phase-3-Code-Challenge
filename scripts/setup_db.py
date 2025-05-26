# scripts/setup_db.py
from lib.db.connection import get_connection

def init_db():
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()