# scripts/run_queries.py
from lib.db.connection import get_connection
from lib.models.author import Author
from lib.models.magazine import Magazine

def authors_for_magazine(magazine_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT a.* FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        WHERE ar.magazine_id = ?
    """, (magazine_id,))
    rows = cursor.fetchall()
    conn.close()
    return [Author(row['name'], row['id']) for row in rows]

def magazines_with_multiple_authors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.* FROM magazines m
        JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
        HAVING COUNT(DISTINCT a.author_id) >= 2
    """)
    rows = cursor.fetchall()
    conn.close()
    return [Magazine(row['name'], row['category'], row['id']) for row in rows]

def article_counts_per_magazine():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT m.name, COUNT(a.id) as article_count
        FROM magazines m
        LEFT JOIN articles a ON m.id = a.magazine_id
        GROUP BY m.id
    """)
    rows = cursor.fetchall()
    conn.close()
    return [(row['name'], row['article_count']) for row in rows]

def most_prolific_author():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT a.* FROM authors a
        JOIN articles ar ON a.id = ar.author_id
        GROUP BY a.id
        ORDER BY COUNT(ar.id) DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    conn.close()
    return Author(row['name'], row['id']) if row else None

if __name__ == "__main__":
    print("Authors for magazine ID 1:", [a.name for a in authors_for_magazine(1)])
    print("Magazines with multiple authors:", [m.name for m in magazines_with_multiple_authors()])
    print("Article counts per magazine:", article_counts_per_magazine())
    author = most_prolific_author()
    print("Most prolific author:", author.name if author else None)