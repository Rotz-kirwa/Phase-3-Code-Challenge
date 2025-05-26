# lib/db/seed.py
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
from lib.db.connection import get_connection

def seed_data():
    conn = get_connection()
    try:
        conn.execute("DELETE FROM articles")
        conn.execute("DELETE FROM authors")
        conn.execute("DELETE FROM magazines")
        conn.execute("DELETE FROM sqlite_sequence")
        conn.commit()
        
        conn.execute("BEGIN TRANSACTION")
        
        # Create authors
        author1 = Author("John Doe")
        author1.save()
        author2 = Author("Jane Smith")
        author2.save()
        author3 = Author("Alice Johnson")
        author3.save()

        # Create magazines
        magazine1 = Magazine("Tech Today", "Technology")
        magazine1.save()
        magazine2 = Magazine("Science Weekly", "Science")
        magazine2.save()

        # Create articles
        Article("Tech Trends", author1, magazine1).save()
        Article("AI Revolution", author1, magazine1).save()
        Article("Quantum Computing", author2, magazine1).save()
        Article("Climate Change", author2, magazine2).save()
        Article("Space Exploration", author3, magazine2).save()
        Article("Gadget Reviews", author1, magazine1).save()

        conn.commit()
        print("Database seeded successfully.")
    except Exception as e:
        conn.rollback()
        print(f"Seeding failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    seed_data()