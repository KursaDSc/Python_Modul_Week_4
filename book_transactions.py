import core.data_io as di

#kitaplarin kayitli oldugu dosya
books_file = 'data/books.json'

#kitap ekleme
def add_book(barcode, title , publisher, author, status):
    books = di.read_json(books_file)
    books.append({
        'barcode': barcode,
        'title': title,
        'publisher': publisher,
        'author': author,
        'status': status
    })
    di.write_json(books_file, books)
#kitap silme
def delete_book(barcode):
    books = di.read_json(books_file)
    books = [book for book in books if book['barcode'] != barcode]
    di.write_json(books_file, books)
#kitap silme
def search_book(search_term):
    books = di.read_json(books_file)
    results = []
    for book in books:
        if (search_term.lower() in book['title'].lower() or
            search_term.lower() in book['author'].lower() or
            search_term.lower() in book['publisher'].lower()):
            results.append(book)
    return results
#kitaplari listeleme
def get_all_books():
    books = di.read_json(books_file)
    return books
#kitap durumunu kontrol etme
def is_book_available(barcode):
    books = di.read_json(books_file)
    for book in books:
        if book['barcode'] == barcode:
            return book['status'] == 'available'
    return False