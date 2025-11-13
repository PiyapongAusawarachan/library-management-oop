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