import os
import json
import core.data_io
#kitaplarin kayitli oldugu dosya
books_file = 'data/books.json'
books = []


def add_book(barcode, title , publisher, author, status):
    books = data_io.read_json(books_file)
    books.append({
        'barcode': barcode,
        'title': title,
        'publisher': publisher,
        'author': author,
        'status': status
    })

def delete_book(barcode):
    books = [book for book in books if book['barcode'] != barcode]

def search_book(search_term):
    results = []
    for book in books:
        if (search_term.lower() in book['title'].lower() or
            search_term.lower() in book['author'].lower() or
            search_term.lower() in book['publisher'].lower()):
            results.append(book)
    return results

def get_all_books():
    books = data_io.read_json(books_file)
    return books

def is_book_available(barcode):
    for book in books:
        if book['barcode'] == barcode:
            return book['status'] == 'available'
    return False