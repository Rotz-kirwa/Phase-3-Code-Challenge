# lib/models/article.py
from lib.db.connection import get_connection

class Article:
    def __init__(self, title, author, magazine, id=None):
        self.id = id
        self.title = title
        self.author = author
        self.magazine = magazine

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Title must be a non-empty string")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        from lib.models.author import Author
        if not isinstance(value, Author):
            raise ValueError("Author must be an Author instance")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        from lib.models.magazine import Magazine
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be a Magazine instance")
        self._magazine = value

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        try:
            if self.id is None:
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id",
                    (self.title, self.author.id, self.magazine.id)
                )
                self.id = cursor.fetchone()[0]
            else:
                cursor.execute(
                    "UPDATE articles SET title = ?, author_id = ?, magazine_id = ? WHERE id = ?",
                    (self.title, self.author.id, self.magazine.id, self.id)
                )
            conn.commit()
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            conn.close()

    @classmethod
    def find_by_id(cls, id):
        from lib.models.author import Author
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            author = Author.find_by_id(row['author_id'])
            magazine = Magazine.find_by_id(row['magazine_id'])
            return cls(row['title'], author, magazine, row['id'])
        return None