# scripts/setup_db.py

import os
from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        schema_sql = f.read()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
    print("Database schema created successfully!")

if __name__ == "__main__":
    # Delete existing DB file to start fresh
    if os.path.exists('articles.db'):
        os.remove('articles.db')
    setup_database()
