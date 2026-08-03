class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_book(self):
        if self.is_borrowed == True:
            self.is_borrowed = False
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

