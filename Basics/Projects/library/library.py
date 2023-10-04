import csv

def read_lib(library):
    with open(library) as file:
        reader = csv.DictReader(file)
        return [row for row in reader]

def search_author(books, author):
    return [book for book in books if book['author'] == author]

def search_by_isbn(books, isbn):
    for book in books:
        if book['ISBN'] == isbn:
            return {'title': book['title'], 'price': book['price']}
    return None

def search_books_by_price_range(books, min_price, max_price):
    return [book for book in books if min_price <= float(book['price']) <= max_price]

def add_book_to_csv(library, book):
    with open(library, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(book)

if __name__ == '__main__':
    library = 'library.csv'
    books = read_lib(library)

    while True:
        print('1. Search books by author')
        print('2. Search book by ISBN')
        print('3. Search books by price range')
        print('4. Add new book')
        print('5. quit')

        choice = input('Enter your choice: ')

        if choice == '1':
            author = input('Enter author name: ')
            result = search_author(books, author)
            if result:
                print(f'Books written by {author}:')
                for book in result:
                    print(f'{book["title"]} ({book["ISBN"]}) - {book["price"]}')
            else:
                print(f'No books found written by {author}')

        elif choice == '2':
            isbn = input('Enter ISBN: ')
            result = search_by_isbn(books, isbn)
            if result:
                print(f'Title: {result["title"]}, Price: {result["price"]}')
            else:
                print(f'No book found with ISBN {isbn}')

        elif choice == '3':
            min_price = float(input('Enter minimum price: '))
            max_price = float(input('Enter maximum price: '))
            result = search_books_by_price_range(books, min_price, max_price)
            if result:
                print(f'Books within price range {min_price} to {max_price}:')
                for book in result:
                    print(f'{book["title"]} ({book["ISBN"]}) - {book["price"]}')
            else:
                print(f'No books found within price range {min_price} to {max_price}')

        elif choice == '4':
            title = input('Enter title: ')
            author = input('Enter author: ')
            isbn = input('Enter ISBN: ')
            price = input('Enter price: ')
            add_book_to_csv(library, [title, author, isbn, price])
            print(f'Book added successfully')

        elif choice == '5':
            break

        else:
            print('Invalid choice')
