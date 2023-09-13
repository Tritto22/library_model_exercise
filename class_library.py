from class_book import Book

class Library:
    def __init__(self):
        self.catalogue=[]
        self.genres=dict()

    def add_book(self, book):
        self.catalogue.append(book)
        if book.genre in self.genres:
            # Se il genere esiste, aggiungi il libro alla lista esistente
            self.genres[book.genre].append(book)
        else:
            # Se il genere non esiste, crea una nuova lista con il libro
            self.genres[book.genre] = [book]

    def print_genres(self):
        for genre, books in self.genres.items():
            print(f"Genere: {genre}")
            for book in books:
                print(f"  Titolo: {book.title}, Autore: {book.author}")

#exemple function
b1=Book('La fisica','Bensi', 'scienze')
b2=Book('Il cuore','Rossi', 'passioni')
b3=Book('il Giallo','Neri', 'gialli')
b4=Book('Poemetti','Bianchi', 'poetica')
b5=Book('La matematica','Bensi', 'scienze')
b6=Book('La chimica','Bensi', 'scienze')
b7=Book('L\'assassino','Verdi', 'gialli')

library=Library()
library.add_book(b1)
library.add_book(b2)
library.add_book(b3)
library.add_book(b4)
library.add_book(b5)
library.add_book(b6)
library.add_book(b7)
