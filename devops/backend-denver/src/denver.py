from flask import Flask
import json
from random import randrange

app = Flask(__name__)

fichier = open("/home/books.json", "r")
books = json.load(fichier)

@app.route("/book", methods=['GET'])
def get_random_book():
    r = randrange(1,5)
    for book in books:
        if str(book['id']) == str(r):
            return book

    return 404

