from Utils import database


def menu():
    user_input = input("User Choice: ")
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input == "l":
            list_book()
        elif user_input == "r":
            read_book()
        elif user_input == "d":
            delete_book()
        else:
            print("Unkown command. Please try again")

        user_input = input("User Choice: ")

def prompt_add_book():
    name = input("Enter the book name: ")
    author = input("Enter the author's name: ")

    database.add_book_name(name,author)




def list_book():
    books = database.view_books()
    for book in books:
        print(f'{book["name"]} by {book["author"]}, read: {book["read"]}')

def read_book():
    name = input("Enter the name of the book you just finished reading: ")

    database.mark_book_as_read(name)

def delete_book():
    name =input("Enter the name of the book you want to delete: ")

    database.remove_book(name)

menu()

