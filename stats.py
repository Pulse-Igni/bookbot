# Stat functions for analyzing books:
def word_counter(book):
        splitnum = book.split()
        count = len(splitnum)
        return count

def char_counter(book):
    char_count = {}
    lower_cased = book.lower()
    for char in lower_cased:
          if char in char_count:
                char_count[char] += 1
          else:
                char_count[char]=1
    return (char_count)


def report (book,locale):
      print ("============ BOOKBOT ============")
      print (f"Analyzing book found at {locale}")
      print ("----------- Word Count ----------")
      print (f"Found {word_counter(book)} total words")
      print ("-------- Character Count --------")
      char_unsorted = char_counter(book)
      sorted_chars = sorted(char_unsorted, key=char_unsorted.get, reverse=True) 
      for keys in sorted_chars:
            if keys.isalpha():
                  print (keys, char_unsorted[keys])
      print("=============== END ==============")
      
