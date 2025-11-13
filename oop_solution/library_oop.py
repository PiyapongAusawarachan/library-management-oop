class Book:
    def __init__(self, id, title, author, total):
        self.id = id
        self.title = title
        self.author = author
        self.total = total
        self.available = total

    def borrow_copy(self):
        if self.available > 0:
            self.available -= 1
            return True
        return False

    def return_copy(self):
        if self.available < self.total:
            self.available += 1
            return True
        return False


class Member:
    def __init__(self, mid, fullname, mail="N/A"):
        self.mid = mid
        self.fullname = fullname
        self.mail = mail
        self.books = []

    def borrow_book(self, bk):
        if len(self.books) >= 3:
            print("Error: Borrow limit reached!")
            return False
        if not bk.borrow_copy():
            print("Error: No copies left!")
            return False
        self.books.append(bk)
        print(f"{self.fullname} borrowed '{bk.title}'")
        return True

    def return_book(self, bk):
        if bk not in self.books:
            print("Error: Book not borrowed!")
            return False
        self.books.remove(bk)
        bk.return_copy()
        print(f"{self.fullname} returned '{bk.title}'")
        return True
