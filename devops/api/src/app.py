from flask import Flask
import json

app = Flask(__name__)

fichier = open("/home/books.json", "r")
books = json.load(fichier)

@app.route("/book/<identifient>", methods=['POST', 'GET'])
def get_book_par_ident(identifient):
    for book in books:
        if str(book['id']) == str(identifient):
            return book

    return 404

@app.route("/books", methods=['GET'])
def get_tout_livre():
    return books
