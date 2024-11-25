# -*- coding: utf-8 -*-
"""Observer.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10H87aLYg6N2v6LpaBddyqVJRSx21I6hM
"""

class LibraryCatalog:
    def __init__(self):
        self.books = []
        self.observers = []

    def add_book(self, title, available=True):
        self.books.append({"title": title, "available": available})
        if available:
            self.notify_observers(title)

    def change_book_status(self, title, available):
        for book in self.books:
            if book["title"].lower() == title.lower():
                book["available"] = available
                if available:
                    self.notify_observers(title)
                return f"'{title}' status changed to {'available' if available else 'borrowed'}."
        return f"'{title}' not found."

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, book_title):
        for observer in self.observers:
            observer.update(book_title)


class User:
    def __init__(self, name):
        self.name = name

    def update(self, book_title):
        print(f"{self.name} has been notified: '{book_title}' is now available!")


if __name__ == "__main__":
    catalog = LibraryCatalog()

    # Creating users
    kasia = User("Kasia")
    jan = User("Jan")

    # Adding observers
    catalog.add_observer(kasia)
    catalog.add_observer(jan)

    # Adding books
    print(catalog.add_book("Fajna Książka", available=False))
    print(catalog.add_book("Śmieszna Opowieść"))

    # Changing book status
    print(catalog.change_book_status("Śmieszna Opowieść", available=False))
    print(catalog.change_book_status("Fajna Książka", available=True))