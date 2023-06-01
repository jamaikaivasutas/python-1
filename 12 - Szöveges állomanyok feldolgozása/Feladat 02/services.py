from book import Book
from typing import *

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)

def getBooksByTheme(theme: str, books: List[Book]) -> List[Book]:
    filteredBooks: List[Book] = []
    
    for book in books:
        if(book.theme == theme):
            filteredBooks.append(book)

    return filteredBooks

def getBooksByPublishYearIntelval(start: int, end: int, books: List[Book]) -> List[Book]:
    filteredBooks: List[Book] = []
    
    for book in books:
        if(book.publishYear >= start and book.publishYear <= end):
            filteredBooks.append(book)

    return filteredBooks

def sortBooksByPageNumberDescending(books: List[Book]) -> None:
    booksCount: int = len(books)
    temp: Book = None

    for i in range(0, booksCount - 1, 1):
        for j in range(i+1, booksCount, 1):
            if(books[j].pageNumber > books[i].pageNumber):
                temp = books[i]
                books[i] = books[j]
                books[j] = temp
