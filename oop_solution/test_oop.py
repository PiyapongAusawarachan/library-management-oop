from library_oop import Book, Member, Library

def test_library():
    print("="*50)
    print("START TEST")
    print("="*50)

    lib = Library()

    print("\nTEST: add books")
    lib.add_book(1, "Python Crash Course", "Eric Matthes", 3)
    lib.add_book(2, "Clean Code", "Robert C. Martin", 2)
    lib.add_book(3, "The Pragmatic Programmer", "Andrew Hunt", 1)
    lib.add_book(4, "Design Patterns", "GoF", 2)

    print("\nTEST: add members")
    lib.add_member(101, "Alice Smith", "alice@mail.com")
    lib.add_member(102, "Bob Jones", "bob@mail.com")
    lib.add_member(103, "Carol White", "carol@mail.com")

    print("\nTEST: show books (initial)")
    lib.show_books()

    print("\nTEST: borrow success")
    print(lib.borrow_book(101, 1))
    print(lib.borrow_book(101, 2))
    print(lib.borrow_book(102, 1))

    print("\nTEST: member books")
    lib.show_member_books(101)
    lib.show_member_books(102)
    lib.show_member_books(103)

    print("\nTEST: show books (after borrow)")
    lib.show_books()

    print("\nTEST: borrow last copy and fail when none left")
    print(lib.borrow_book(103, 3))
    print(lib.borrow_book(102, 3))

    print("\nTEST: borrow limit")
    print(lib.borrow_book(101, 4))
    lib.show_member_books(101)
    print(lib.borrow_book(101, 3))

    print("\nTEST: returns")
    print(lib.return_book(101, 1))
    print(lib.return_book(102, 1))
    lib.show_member_books(101)
    lib.show_books()

    print("\nTEST: invalid return")
    print(lib.return_book(102, 2))

    print("\nTEST: return and reborrow")
    print(lib.return_book(103, 3))
    print(lib.borrow_book(102, 3))
    lib.show_member_books(102)

    print("\nTEST: error cases")
    print(lib.borrow_book(999, 1))
    print(lib.borrow_book(101, 999))
    print(lib.return_book(999, 1))
    lib.show_member_books(999)

    print("\nTEST: final state")
    for m in lib.member_list:
        print(m.fullname, [b.title for b in m.books])
    lib.show_books()

    print("\n" + "="*50)
    print("END TEST")
    print("="*50)

if __name__ == "__main__":
    test_library()
