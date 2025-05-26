# Magazine Article Management System

A Python application that models the relationships between Authors, Articles, and Magazines using a SQLite database with raw SQL queries.

## Overview

This project implements a simple content management system for magazine articles with three main models:
- **Author**: Represents writers who create articles
- **Magazine**: Represents publications that contain articles
- **Article**: Represents content written by authors for specific magazines

## Features

- Create and manage authors, magazines, and articles
- Track which authors contribute to which magazines
- Find all articles by a specific author
- Find all articles in a specific magazine
- Identify authors who have written more than 2 articles for a magazine
- Find the magazine with the most articles

## Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd sql-alchemy-code-challenge
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
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

## Usage

You can interact with the application using the debug console:

```bash
python -m lib.debug
```

### Example operations:

```python
# Find an author
author = Author.find_by_name("John Doe")

# Get all articles by an author
articles = author.articles()

# Find a magazine
magazine = Magazine.find_by_name("Tech Today")

# Get all articles in a magazine
articles = magazine.articles()

# Create a new article
new_article = author.add_article(magazine, "New Article Title")
```

## Testing

Run the tests with pytest:

```bash
python -m pytest
```

## Project Structure

- `lib/models/`: Contains the model classes (Author, Magazine, Article)
- `lib/db/`: Database connection and schema files
- `scripts/`: Utility scripts for database setup
- `tests/`: Test files for each model

## License

