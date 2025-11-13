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


class Library:
    def __init__(self):
        self.book_list = []
        self.member_list = []
        self.records = []

    def add_book(self, bid, title, writer, total):
        if any(b.id == bid for b in self.book_list):
            print(f"Error: Book ID {bid} already exists!")
            return
        bk = Book(bid, title, writer, total)
        self.book_list.append(bk)
        print(f"Book '{bk.title}' added successfully!")

    def find_book(self, bid):
        for b in self.book_list:
            if b.id == bid:
                return b
        return None

    def add_member(self, mid, fullname, mail="N/A"):
        if any(m.mid == mid for m in self.member_list):
            print(f"Error: Member ID {mid} already exists!")
            return
        mem = Member(mid, fullname, mail)
        self.member_list.append(mem)
        print(f"Member '{mem.fullname}' registered successfully!")

    def find_member(self, mid):
        for m in self.member_list:
            if m.mid == mid:
                return m
        return None

    def borrow_book(self, mid, bid):
        mem = self.find_member(mid)
        bk = self.find_book(bid)
        if not mem:
            print("Error: Member not found!")
            return False
        if not bk:
            print("Error: Book not found!")
            return False
        if mem.borrow_book(bk):
            self.records.append({"mid": mem.mid, "mname": mem.fullname, "bid": bk.id, "btitle": bk.title})
            return True
        return False

    def return_book(self, mid, bid):
        mem = self.find_member(mid)
        bk = self.find_book(bid)
        if not mem or not bk:
            print("Error: Member or book not found!")
            return False
        if mem.return_book(bk):
            self.records = [r for r in self.records if not (r["mid"] == mem.mid and r["bid"] == bk.id)]
            return True
        return False

    def show_books(self):
        print("\n=== Available Books ===")
        for b in self.book_list:
            if b.available > 0:
                print(f"{b.title} by {b.author} - {b.available} copies")

    def show_member_books(self, mid):
        mem = self.find_member(mid)
        if not mem:
            print("Error: Member not found!")
            return
        print(f"\n=== Books borrowed by {mem.fullname} ===")
        if mem.books:
            for bk in mem.books:
                print(f"- {bk.title} by {bk.author}")
        else:
            print("No books borrowed")
