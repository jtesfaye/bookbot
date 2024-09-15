from collections import Counter

def wordCount(book):
    words = book.split()
    print(f"There are {len(words)} in this book\n")
    return words


def openBook(book):
    with open(book) as f:
        file_contents = f.read()
        words = file_contents
        f.close()
    return words

def countCharacters(words): 
    lowered = words.lower()
    wordC = Counter(lowered)
    return dict(sorted(wordC.items()))

    


if __name__ == "__main__":


    book = "books/frankenstein.txt"

    print(f"--- Begin report of {book} ---")
    words = openBook(book)
    wordList = wordCount(words)
    charList = countCharacters(words)

    for i in charList:
        if i.isalpha():
            print(f"The {i} character was found {charList[i]} times")

    

    
    
