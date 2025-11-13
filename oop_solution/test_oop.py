from library_oop import Book, Member

b1 = Book(1, "Python 101", "John", 2)
b2 = Book(2, "C++ Basics", "Jane", 1)
m = Member(1, "Alice", "alice@mail.com")

print(b1.available)
m.borrow_book(b1)
print(b1.available)
m.borrow_book(b2)
print(b2.available)
m.return_book(b1)
print(b1.available)
m.borrow_book(b1)
m.borrow_book(b1)
m.borrow_book(b1)
