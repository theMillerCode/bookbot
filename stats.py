from get_book import get_book_text

#count the # of words in book
def num_of_words():
    word_count = get_book_text().split()
    return f"{len(word_count)} words found in the document"