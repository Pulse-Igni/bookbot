# Import
from stats import word_counter 
from stats import char_counter


# Retrieve book from:
def get_book_text(address):
    with open(address) as book:
        book_contents = book.read()
    return book_contents


def main(book):   
    word_counter(get_book_text(book))
    char_counter(get_book_text(book))


# Book to read from:
frankenstein = "books/frankenstein.txt"
book = frankenstein

main(book)