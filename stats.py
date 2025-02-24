from get_book import get_book_text
from letter_counts import count_letters

#count the # of words in book
def num_of_words():
    word_count = get_book_text().split()
    return f"Found {len(word_count)} total words"

#count each character in the book
def char_count():
    #split book into seperate char
    #book = [*get_book_text().lower()]
    
    #count each char 
    count_of_t = count_letters([*get_book_text().lower()])

    sorted_dict = dict(sorted(count_of_t.items(), key=lambda item: item[1], reverse=True))


    return sorted_dict
