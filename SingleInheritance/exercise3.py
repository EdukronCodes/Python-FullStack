# Base Class
class Book:
    def __init__(self, title):
        self.title = title
        print(f"[Book] Title: {self.title}")

    def read(self):
        print(f"[Book] Reading {self.title}")

# Derived Class
class Novel(Book):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author
        print(f"[Novel] Author: {self.author}")

    def read(self):
        print(f"[Novel] {self.title} by {self.author}")

# Object creation and method calls
my_novel = Novel("1984", "George Orwell")
my_novel.read()
my_novel.read() 