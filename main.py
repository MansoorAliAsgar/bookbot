import sys
import string

def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_book(book_path)
    word_count = get_word_count(file_contents)
    letter_count = get_letter_count(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in document")
    count = 0
    for key, value in letter_count.items():
        if value > 0 and key.isalpha():
            count += 1
            print(f"the '{key}' character was found {value} times\n")
    

def get_book(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(file_contents):
    words = file_contents.split()
    word_count = len(words)
    return word_count

def get_letter_count(file_contents):
    res_dict = {}
    file_contents_ci = file_contents.lower()
    alphabets = list(string.ascii_lowercase)
    sp_char = list(string.punctuation)
    all_char = alphabets + sp_char
    for character1 in all_char:
        res_dict[character1] = 0
        for character2 in file_contents_ci:
            if character1 == character2:
                res_dict[character1] += 1
    return res_dict


if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit
