from stats import num_of_words
from stats import char_count
from get_book import set_path
import sys

def main():

# Your program's main logic goes here

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {set_path()}...")

    print("----------- Word Count ----------")
    print(num_of_words())

    print("--------- Character Count -------")
    
    #asked google how to add return after each dic item
    for key, value in char_count().items():
        print(f"{key}: {value}\n", end="")

    print("============= END ===============")

main()