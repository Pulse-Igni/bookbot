# Stat functions for analyzing books:
def word_counter(book):
        splitnum = book.split()
        count = len(splitnum)
        print (f"{count} words found in the document")

def char_counter(book):
    char_count = {}
    lower_cased = book.lower()
    for char in lower_cased:
          if char in char_count:
                char_count[char] += 1
          else:
                char_count[char]=1
    print (char_count)




#testing block
#testing = "String, and returns the number of times each character, (including symbols and spaces),"

#char_counter(testing)