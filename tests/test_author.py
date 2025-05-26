# tests/test_author.py
import pytest
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.db.connection import get_connection
from scripts.setup_db import init_db
from lib.db.seed import seed_data

@pytest.fixture(autouse=True)
def setup_db():
    init_db()
    seed_data()

def test_author_initialization():
    author = Author("Test Author")
    assert author.name == "Test Author"
    with pytest.raises(ValueError):
        Author("")

def test_author_save():
    author = Author("New Author")
    author.save()
    saved = Author.find_by_name("New Author")
    assert saved is not None
    assert saved.name == "New Author"

def test_author_articles():
    author = Author.find_by_name("John Doe")
    articles = author.articles()
    assert len(articles) == 3
    assert all(a.author.id == author.id for a in articles)

def test_author_magazines():
    author = Author.find_by_name("John Doe")
    magazines = author.magazines()
    assert len(magazines) == 1
    assert magazines[0].name == "Tech Today"

def test_author_add_article():
    author = Author.find_by_name("Jane Smith")
    magazine = Magazine.find_by_name("Tech Today")
    article = author.add_article(magazine, "New Article")
    assert article.title == "New Article"
    assert article.author.id == author.id
    assert article.magazine.id == magazine.id

def test_author_topic_areas():
    author = Author.find_by_name("Jane Smith")
    topics = author.topic_areas()
    assert set(topics) == {"Technology", "Science"}