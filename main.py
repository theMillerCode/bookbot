path = "books/frankenstein.txt"

def main():
    with open(path) as f:
        #variables
        file_contents = f.read()
        char_set = set(file_contents.lower())
        new_dict = {}
        count = 0

        #functions
        def sort_on(dict):
            return dict["num"]

        print(f"--- Begin report of {path} ---")

        print(len(file_contents.split()), "words found in the document")

        for char in char_set:
            new_dict.update({char : file_contents.lower().count(char) })

        list_of_dicts = [{'letter': key, 'num': value} for key, value in new_dict.items()]

        list_of_dicts.sort(reverse=True, key=sort_on)

        for dicts in list_of_dicts:
            items = list(dicts.items())
            first_key, first_value = items[0]
            second_key, second_value = items[1]

            if first_value.isalpha():
                print(f"The '{first_value}' character was found {second_value} times")

            
main()