# tests/test_magazine.py
import pytest
from lib.models.magazine import Magazine
from lib.models.author import Author
from lib.db.connection import get_connection
from scripts.setup_db import init_db
from lib.db.seed import seed_data

@pytest.fixture(autouse=True)
def setup_db():
    init_db()
    seed_data()

def test_magazine_initialization():
    magazine = Magazine("Test Mag", "Test Cat")
    assert magazine.name == "Test Mag"
    assert magazine.category == "Test Cat"
    with pytest.raises(ValueError):
        Magazine("", "Category")

def test_magazine_save():
    magazine = Magazine("New Mag", "New Cat")
    magazine.save()
    saved = Magazine.find_by_name("New Mag")
    assert saved is not None
    assert saved.category == "New Cat"

def test_magazine_articles():
    magazine = Magazine.find_by_name("Tech Today")
    articles = magazine.articles()
    assert len(articles) == 3
    assert all(a.magazine.id == magazine.id for a in articles)

def test_magazine_contributors():
    magazine = Magazine.find_by_name("Tech Today")
    contributors = magazine.contributors()
    assert len(contributors) == 2
    assert set(a.name for a in contributors) == {"John Doe", "Jane Smith"}

def test_magazine_article_titles():
    magazine = Magazine.find_by_name("Tech Today")
    titles = magazine.article_titles()
    assert set(titles) == {"Tech Trends", "AI Revolution", "Quantum Computing"}

def test_magazine_contributing_authors():
    magazine = Magazine.find_by_name("Tech Today")
    contributors = magazine.contributing_authors()
    assert len(contributors) == 1
    assert contributors[0].name == "John Doe"

def test_top_publisher():
    magazine = Magazine.top_publisher()
    assert magazine.name == "Tech Today"