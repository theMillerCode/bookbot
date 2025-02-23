#get the book to analyse
def get_book_text():
    #filepath
    path_to_file = "books/frankenstein.txt"

    #open file
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#count the # of words in book
def num_of_words():
    word_count = get_book_text().split()
    return f"{len(word_count)} words found in the document"
    
def main():
    print(num_of_words())

main()