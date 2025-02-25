import sys
from stats import word_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        word_int = word_count(file_contents)
        char_dict = char_count(file_contents)
        sorted_list = chars_dict_to_sorted_list(char_dict)
        print("--- Begin report of books/frankenstein.txt ---")
        print()
        print(f"{word_int} words found in the document")

        for item in sorted_list:
            if item["char"].isalpha():
                print(f"The '{item['char']}' character was found {item['num']} times")

        print("--- End report ---")


def sort_on(d):
    return d["num"]
    
def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def char_count(string):
    chars = {}
    for c in string:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()