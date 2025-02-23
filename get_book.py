#get the book to analyse
def get_book_text():
    #filepath
    path_to_file = "books/frankenstein.txt"

    #open file
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents