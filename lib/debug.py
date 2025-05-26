# lib/debug.py
from scripts.setup_db import init_db
from lib.db.seed import seed_data
from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article
import code

init_db()
seed_data()
code.interact(local=locals())