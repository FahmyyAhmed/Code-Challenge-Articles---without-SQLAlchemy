# scripts/setup_db.py

from lib.db.connection import get_connection

def setup_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Read and execute schema.sql
    with open('lib/db/schema.sql') as f:
        cursor.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database setup complete.")

if __name__ == "__main__":
    setup_database()

    # Seed data after setup
    from lib.db.seed import seed_data
    seed_data()
