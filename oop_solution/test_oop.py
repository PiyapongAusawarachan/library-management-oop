from library_oop import Book

b = Book(1, "Python 101", "John Doe", 3)

print(b.available)
b.borrow_copy()
print(b.available)
b.borrow_copy()
print(b.available)
b.return_copy()
print(b.available)
b.return_copy()
print(b.available)
