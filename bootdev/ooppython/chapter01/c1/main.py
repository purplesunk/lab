class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author


class Library:
    def __init__(self, name):
        self.books = []
        self.name = name

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        print_books(self.books)
        for i in range(0, len(self.books) - 1):
            r_title = self.books[i].title == book.title
            r_author = self.books[i].author == book.author
            if r_title and r_author:
                self.books.pop(i)

    def search_books(self, search_string):
        matches = []
        search_string_l = search_string.lower()
        for book in self.books:
            r_title = book.title.lower().find(search_string_l)
            r_author = book.author.lower().find(search_string_l)
            if r_title != -1 or r_author != -1:
                matches.append(book)

        return matches
