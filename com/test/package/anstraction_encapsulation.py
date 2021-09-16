# Abstraction and encapsulation

class library:
    def __init__(self, books):
        self._books = books

    def list_books(self):
        print("Available books")
        for book in self._books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self._books:
            print("Get your book")
            self._books.remove(borrow_book)
        else:
            print("Book not available")

    def receive_book(self, receive_book):
        print("You ahve returned the book")
        self._books.append(receive_book)

books = ['C', 'C++', 'Python']

o = library(books)

msg = """
      1. Display books
      2. Borrow Books
      3. Return Books
      4. Exit  
        """
while True:
    print(msg)
    ch = int(input("Enter your choice: "))
    if ch == 1:
        o.list_books()
    elif ch == 2:
        book = input("Enter the book name for borrowing: ")
        o.borrow_book(book)
    elif ch == 3:
        book = input("Enter the book name to return: ")
        o.receive_book(book)
    else:
        print("Thank you come again")
        quit()