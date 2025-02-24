def set_path():
    #filepath
    path_to_file = "books/frankenstein.txt"
    return path_to_file

#get the book to analyse
def get_book_text():
    #filepath
    path = set_path()

    #open file
    with open(path) as f:
        file_contents = f.read()
    return file_contents