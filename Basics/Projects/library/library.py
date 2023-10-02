# Create a program that reads in a CSV file containing information about books (title, author, ISBN, and price), and then allows the user to search for books by author, ISBN, or price range.
# Step 1: Create a function that takes a file name as an argument and reads in the contents of the file as a list of dictionaries, with each dictionary representing a book and containing keys for title, author, ISBN, and price.
# Step 2: Create a function that takes an author's name as an argument and returns a list of all books written by that author.
# Step 3: Create a function that takes an ISBN as an argument and returns the title and price of the book with that ISBN.
# Step 4: Create a function that takes a minimum and maximum price as arguments and returns a list of all books within that price range.
# Step 5: Use the functions from steps 2-4 in a user interface that allows the user to search for books by author, ISBN, or price range.
# Bonus: Add the ability for the user to add new books to the CSV file.

import csv

def open_file('library.csv'):
    books = []
    with open('library.csv','r')as lib1:
        user = csv.DictReader(lib1)
        for row in user:
            books.append(row)
    return books
def search_author(books,author):
    results = []
    for book in books:
        if book['author'] == author:
            results.append(book)
    return results
def search_isbn(books,isbn):
    for book in books:
        if book['ISBN'] == isbn:
            return book['title'],book['price'],book['author']
    return None, None
def search_price(books,price):
    results = []
    for book in books:
        price = float(book['price'])
        return results.append(book)
    return results
def input():

    library = 'library.csv'

    books = read_csv(library)

    while True:
        print('Search type:')
        print('1. Author')
        print('2.ISBN')
        print('Price')

        input = ('Enter your choice:')

        if input
    



