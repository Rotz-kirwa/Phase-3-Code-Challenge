# tests/test_article.py
import pytest
from lib.models.article import Article
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection
from scripts.setup_db import init_db
from lib.db.seed import seed_data

@pytest.fixture(autouse=True)
def setup_db():
    init_db()
    seed_data()

def test_article_initialization():
    author = Author.find_by_name("John Doe")
    magazine = Magazine.find_by_name("Tech Today")
    article = Article("Test Article", author, magazine)
    assert article.title == "Test Article"
    assert article.author == author
    assert article.magazine == magazine
    with pytest.raises(ValueError):
        Article("", author, magazine)

def test_article_save():
    author = Author.find_by_name("Jane Smith")
    magazine = Magazine.find_by_name("Science Weekly")
    article = Article("New Article", author, magazine)
    article.save()
    saved = Article.find_by_id(article.id)
    assert saved is not None
    assert saved.title == "New Article"
    assert saved.author.id == author.id
    assert saved.magazine.id == magazine.id