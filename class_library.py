from class_book import Book

class Library:
    def __init__(self):
        self.catalogue=[]
        self.genres=dict()

    def add_book(self, book):
        self.catalogue.append(book)
        self.genres[book.genre]=book


#exemple function
b1=Book('La fisica','Bensi', 'scienze')
b2=Book('Il cuore','Rossi', 'passioni')
b3=Book('il Giallo','Neri', 'gialli')
b4=Book('Poemetti','Bianchi', 'poetica')

library=Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)
