# lib/db/seed.py

from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    # Insert Authors
    authors = ['Alice Walker', 'John Steinbeck', 'Toni Morrison']
    for name in authors:
        cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))

    # Insert Magazines
    magazines = [('Time', 'News'), ('Vogue', 'Fashion'), ('Scientific American', 'Science')]
    for name, category in magazines:
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (name, category))

    # Insert Articles
    articles = [
        ('The Color Purple Review', 1, 1),
        ('East of Eden Analysis', 2, 2),
        ('Beloved Breakdown', 3, 3)
    ]
    for title, author_id, magazine_id in articles:
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                       (title, author_id, magazine_id))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    seed_data()
    print("Database seeded successfully!")
