import json
import os

class Book:
    def _init_(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._is_borrowed = False

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def isbn(self):
        return self._isbn

    @property
    def is_borrowed(self):
        return self._is_borrowed

    @is_borrowed.setter
    def is_borrowed(self, value):
        if isinstance(value, bool):
            self._is_borrowed = value

    def borrow(self):
        if not self._is_borrowed:
            self._is_borrowed = True
            return True
        return False

    def return_book(self):
        if self._is_borrowed:
            self._is_borrowed = False
            return True
        return False

    def to_dict(self):
        return {
            "title": self._title,
            "author": self._author,
            "isbn": self._isbn,
            "is_borrowed": self._is_borrowed
        }

    def _str_(self):
        status = "Borrowed" if self._is_borrowed else "Available"
        return f"Title: {self._title}, Author: {self._author}, ISBN: {self._isbn}, Status: {status}"


class User:
    def _init_(self, name, user_id):
        self._name = name
        self._user_id = user_id
        self._borrowed_books_isbns = []

    @property
    def name(self):
        return self._name

    @property
    def user_id(self):
        return self._user_id

    @property
    def borrowed_books_isbns(self):
        return self._borrowed_books_isbns.copy()

    def add_borrowed_book_isbn(self, isbn):
        if isbn not in self._borrowed_books_isbns:
            self._borrowed_books_isbns.append(isbn)

    def remove_borrowed_book_isbn(self, isbn):
        if isbn in self._borrowed_books_isbns:
            self._borrowed_books_isbns.remove(isbn)

    def to_dict(self):
        return {
            "name": self._name,
            "user_id": self._user_id,
            "borrowed_books_isbns": self._borrowed_books_isbns
        }

    def _str_(self):
        return f"User: {self._name} (ID: {self._user_id}), Borrowed Books: {len(self._borrowed_books_isbns)}"


class Library:
    def _init_(self, book_file='books.json', user_file='users.json'):
        self._books = {}
        self._users = {}
        self._data_file_books = book_file
        self._data_file_users = user_file
        self._load_data()

    def _load_data(self):
        if os.path.exists(self._data_file_books):
            with open(self._data_file_books, 'r') as f:
                books_data = json.load(f)
                for b in books_data:
                    book = Book(b['title'], b['author'], b['isbn'])
                    book.is_borrowed = b['is_borrowed']
                    self._books[b['isbn']] = book

        if os.path.exists(self._data_file_users):
            with open(self._data_file_users, 'r') as f:
                users_data = json.load(f)
                for u in users_data:
                    user = User(u['name'], u['user_id'])
                    for isbn in u['borrowed_books_isbns']:
                        user.add_borrowed_book_isbn(isbn)
                    self._users[u['user_id']] = user

    def _save_data(self):
        with open(self._data_file_books, 'w') as f:
            json.dump([b.to_dict() for b in self._books.values()], f, indent=4)
        with open(self._data_file_users, 'w') as f:
            json.dump([u.to_dict() for u in self._users.values()], f, indent=4)

    def add_book(self, book):
        if book.isbn in self._books:
            return False
        self._books[book.isbn] = book
        self._save_data()
        return True

    def remove_book(self, isbn):
        if isbn in self._books and not self._books[isbn].is_borrowed:
            del self._books[isbn]
            self._save_data()
            return True
        return False

    def register_user(self, user):
        if user.user_id in self._users:
            return False
        self._users[user.user_id] = user
        self._save_data()
        return True

    def remove_user(self, user_id):
        if user_id in self._users and len(self._users[user_id].borrowed_books_isbns) == 0:
            del self._users[user_id]
            self._save_data()
            return True
        return False

    def borrow_book(self, isbn, user_id):
        if isbn in self._books and user_id in self._users:
            book = self._books[isbn]
            user = self._users[user_id]
            if book.borrow():
                user.add_borrowed_book_isbn(isbn)
                self._save_data()
                return True
        return False

    def return_book(self, isbn, user_id):
        if isbn in self._books and user_id in self._users:
            book = self._books[isbn]
            user = self._users[user_id]
            if isbn in user.borrowed_books_isbns:
                if book.return_book():
                    user.remove_borrowed_book_isbn(isbn)
                    self._save_data()
                    return True
        return False

    def search_book(self, query):
        query = query.lower()
        return [b for b in self._books.values() if query in b.title.lower() or query in b.author.lower() or query in b.isbn]

    def display_all_books(self, show_available_only=False):
        for book in self._books.values():
            if show_available_only and book.is_borrowed:
                continue
            print(book)

    def display_all_users(self):
        for user in self._users.values():
            print(user)

    def display_user_borrowed_books(self, user_id):
        if user_id not in self._users:
            print("User not found.")
            return
        user = self._users[user_id]
        for isbn in user.borrowed_books_isbns:
            print(self._books.get(isbn, f"Book with ISBN {isbn} not found."))


def setup_sample_data():
    library = Library()

    books = [
        ("Introduction to Algorithms", "Cormen", "9780262033848"),
        ("Operating System Concepts", "Silberschatz", "9781118063330"),
        ("Computer Networks", "Tanenbaum", "9780132126953"),
        ("Python Programming", "Zelle", "9781590282755"),
        ("Database System Concepts", "Korth", "9780073523323"),
        ("Artificial Intelligence", "Russell", "9780136042594"),
        ("IoT Fundamentals", "Hanes", "9781587144561"),
        ("Embedded Systems", "Raj Kamal", "9780070151253"),
        ("Data Structures Using C", "Tenenbaum", "9780131997462"),
        ("Digital Logic Design", "Morris Mano", "9780131989245"),
    ]

    for title, author, isbn in books:
        library.add_book(Book(title, author, isbn))

    users = [
        ("Shashwat Singh", "U001"),
        ("Shashwat Dubey", "U002"),
        ("Som Srivastava", "U003"),
        ("Pratham Gupta", "U004"),
        ("Divyansh Singh", "U005"),
        ("Aditya Agrahari", "U006"),
    ]

    for name, user_id in users:
        library.register_user(User(name, user_id))

    library.borrow_book("9781118063330", "U001")
    library.borrow_book("9781590282755", "U003")
    library.borrow_book("9781587144561", "U004")
    library.borrow_book("9780070151253", "U004")
    library.borrow_book("9780136042594", "U005")

    print(" Sample data setup complete.")


def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Register User")
        print("4. Remove User")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. Search Book")
        print("8. Display All Books")
        print("9. Display All Users")
        print("10. Display User's Borrowed Books")
        print("11. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                title = input("Title: ")
                author = input("Author: ")
                isbn = input("ISBN: ")
                print("Book added." if library.add_book(Book(title, author, isbn)) else "Book already exists.")

            elif choice == '2':
                isbn = input("ISBN to remove: ")
                print("Removed." if library.remove_book(isbn) else "Book not found or borrowed.")

            elif choice == '3':
                name = input("User Name: ")
                user_id = input("User ID: ")
                print("User registered." if library.register_user(User(name, user_id)) else "User already exists.")

            elif choice == '4':
                user_id = input("User ID to remove: ")
                print("Removed." if library.remove_user(user_id) else "User not found or has borrowed books.")

            elif choice == '5':
                isbn = input("ISBN: ")
                user_id = input("User ID: ")
                print("Book borrowed." if library.borrow_book(isbn, user_id) else "Borrowing failed.")

            elif choice == '6':
                isbn = input("ISBN: ")
                user_id = input("User ID: ")
                print("Book returned." if library.return_book(isbn, user_id) else "Returning failed.")

            elif choice == '7':
                query = input("Search Query: ")
                results = library.search_book(query)
                for book in results:
                    print(book)

            elif choice == '8':
                only_available = input("Show only available books? (y/n): ").lower() == 'y'
                library.display_all_books(show_available_only=only_available)

            elif choice == '9':
                library.display_all_users()

            elif choice == '10':
                user_id = input("User ID: ")
                library.display_user_borrowed_books(user_id)

            elif choice == '11':
                break

            else:
                print("Invalid option. Try again.")

        except Exception as e:
            print("Error:", e)


if _name_ == "_main_":
    setup_sample_data()  # Run once, then comment
    main()