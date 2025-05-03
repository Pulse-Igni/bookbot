# Import
from stats import word_counter 
from stats import char_counter
from stats import report


# Retrieve book from:
def get_book_text(address):
    with open(address) as book:
        book_contents = book.read()
    return book_contents


def main(book):   
    book_locale = frankenstein
    report(get_book_text(book),book_locale)
    


# Book to read from:
frankenstein = "books/frankenstein.txt"
book = frankenstein

main(book)