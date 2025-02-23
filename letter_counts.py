#ask google for example
def count_letters(text):
    letter_counts = {}
    for letter in text:
        if letter.isalpha():  # Consider only letters
            letter = letter.lower()  # Case-insensitive counting
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

#text = "This is a String with Letters."
#result = count_letters(text)
#print(result)
# Expected output: {'t': 2, 'h': 2, 'i': 3, 's': 3, 'a': 1, 'r': 1, 'n': 1, 'g': 1, 'w': 1, 'l': 1, 'e': 2}