from flask import Flask
import json
from flask_caching import Cache

app = Flask(__name__)
#app.config.from_object('config.Config')
config = {
    "DEBUG": True,
    "CACHE_TYPE": "redis",
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CACHE_KEY_PREFIX": "book",
    "CACHE_REDIS_DB": 0,
    "CACHE_REDIS_HOST": "redis",
    "CACHE_REDIS_PORT": "6379",
    "CACHE_REDIS_URL": 'redis://redis:6379'
}
cache = Cache(app, config=config)

fichier = open("/home/books.json", "r")
books = json.load(fichier)

@app.route("/book/<identifient>", methods=['POST', 'GET'])
@cache.cached(timeout=60, query_string=True)
def get_book_par_ident(identifient):
    for book in books:
        if str(book['id']) == str(identifient):
            return book

    return 404

@app.route("/books", methods=['GET'])
def get_tout_livre():
    return books
