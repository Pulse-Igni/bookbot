# Import
from stats import word_counter 
from stats import char_counter
from stats import report
import sys

def main(book):
    try:   
        book_locale = book
        report(get_book_text(book),book_locale)
    except FileNotFoundError:
        print ("File Not Found. Usage: python3 main.py <path_to_book>")

# Retrieve book from:
def get_book_text(address):
    with open(address) as book:
        book_contents = book.read()
    return book_contents

#sys arg
if len(sys.argv) != 2:
    print ("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]

main(book)