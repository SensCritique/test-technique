from flask import Flask
import json
from flask_caching import Cache

app = Flask(__name__)
app.config.from_object('config.Config')
cache = Cache(app)

fichier = open("/home/books.json", "r")
books = json.load(fichier)

@cache.cached(timeout=30, query_string=True)
@app.route("/book/<identifient>", methods=['POST', 'GET'])
def get_book_par_ident(identifient):
    for book in books:
        if str(book['id']) == str(identifient):
            return book

    return 404

@app.route("/books", methods=['GET'])
def get_tout_livre():
    return books
