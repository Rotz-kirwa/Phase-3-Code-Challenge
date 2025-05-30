# SQL Magazine Article Challenge

A code challenge implementing a magazine article management system using raw SQL queries with SQLite.

## Challenge Overview

This project demonstrates the implementation of a many-to-many relationship between authors and magazines through articles, using raw SQL queries instead of an ORM like SQLAlchemy.

## Models

### Author
- Properties: name
- Relationships: has many articles, has many magazines through articles
- Key methods:
  - `articles()`: Returns all articles written by this author
  - `magazines()`: Returns all magazines this author has contributed to
  - `add_article(magazine, title)`: Creates a new article by this author in the given magazine
  - `topic_areas()`: Returns unique categories of magazines this author has published in

### Magazine
- Properties: name, category
- Relationships: has many articles, has many authors through articles
- Key methods:
  - `articles()`: Returns all articles in this magazine
  - `contributors()`: Returns all authors who have written for this magazine
  - `article_titles()`: Returns the titles of all articles in this magazine
  - `contributing_authors()`: Returns authors who have written more than 2 articles for this magazine
  - `top_publisher()`: Class method that returns the magazine with the most articles

### Article
- Properties: title
- Relationships: belongs to an author, belongs to a magazine
- Key methods:
  - Basic CRUD operations

## Database Structure

The database consists of three tables:
- `authors`: Stores author information
- `magazines`: Stores magazine information
- `articles`: Joins authors and magazines with article details

## Setup Instructions

1. Clone the repository
2. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install pytest
   ```
4. Initialize the database:
   ```bash
   python -m scripts.setup_db
   ```
5. Seed the database with sample data:
   ```bash
   python -m lib.db.seed
   ```

## Testing

Run the tests to verify all functionality:
```bash
python -m pytest
```

## Interactive Console

Explore the models interactively:
```bash
python -m lib.debug
```

Example usage:
```python
# Get an author and their articles
author = Author.find_by_name("John Doe")
articles = author.articles()

# Find magazines by category
author.topic_areas()

# Find prolific authors for a magazine
magazine = Magazine.find_by_name("Tech Today")
prolific_authors = magazine.contributing_authors()
```

## Challenge Requirements

- [x] Implement all model classes with appropriate methods
- [x] Use raw SQL queries (no ORM)
- [x] Create proper relationships between models
- [x] Pass all tests
- [x] Implement proper data validation