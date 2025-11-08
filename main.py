import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    book = get_book_text(filepath)
    num_words = count_words(book)
    characters = count_characters(book)
    sorted_characters = sort_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_characters:
        ch = entry["char"]
        if ch.isalpha():
            print(f"{ch}: {entry['num']}")

if __name__ == "__main__":
    main()

"""
this is my first messsy option with an unnecessary for loop and combining
word counting with the main function, so it can't be separated into a separate .py
#function to take a filepath and return the contents of it as a string
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#function that uses the above get_book_text function to print the contents of that file
#def main():
    #book = get_book_text("books/frankenstein.txt")
    #print(book)

#uses get_book_text to retrieve contents of that file as a string
#then splits it into each word and then uses a for loop to go over words and count each word
def main():
    book = get_book_text("books/frankenstein.txt")
    words = book.split()
    num_words = 0
    for w in words:
        num_words += 1
    print(f"Found {num_words} total words")


#this executes the program by calling the main() function
main()
"""

"""
another option - note function definition order doesn't matter as long as they are all
there once you are calling main

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

main()
"""