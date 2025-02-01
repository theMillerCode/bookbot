def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        char_set = set(file_contents.lower())
        char_dict = {}
        new_dict = {}
        count = 0

        #print(file_contents)

        print("Word count:",len(file_contents.split()))

#print(file_contents.lower().count(" "))

        for char in char_set:
            new_dict.update({char : file_contents.lower().count(char) })
            
        print(new_dict)


    

main()