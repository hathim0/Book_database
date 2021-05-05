books = []

def add_book_name(name, author):
    books.append({"name":name, "author":author, "read": False})

def view_books():
    return books

def mark_book_as_read(name):
    for book in books:
        if book["name"] == name:
            book["read"] = True

# def remove_book(name):
#     for book in books:
#         if book["name"] == name:
#             books.remove(book)

# Generally it is considered as a bad programming practise to delete something
# from a list while we are iterating over it as we did above.

def remove_book(name):
    global books
    books = [book for book in books if book["name"] != name]
    # Here we are using the books available in the global scope
