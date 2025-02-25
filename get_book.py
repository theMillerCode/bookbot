import sys

def set_path():
    #filepath
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = (sys.argv[1])

    #path_to_file = "books/frankenstein.txt"
    return path_to_file

#get the book to analyse
def get_book_text():
    #filepath
    path = set_path()

    #open file
    with open(path) as f:
        file_contents = f.read()
    return file_contents