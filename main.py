def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_int = word_count(file_contents)
        char_dict = char_count(file_contents)
        print(f"book has {word_int} words")
        print(f"letter count: {char_dict}")

def word_count(string):
    words = string.split()
    length = len(words)
    return length

def char_count(string):
    chardict = {
        "a" : 0,
        "b" : 0,
        "c" : 0,
        "d" : 0,
        "e" : 0,
        "f" : 0,
        "g" : 0,
        "h" : 0,
        "i" : 0,
        "j" : 0,
        "k" : 0,
        "l" : 0,
        "m" : 0,
        "n" : 0,
        "o" : 0,
        "p" : 0,
        "q" : 0,
        "r" : 0,
        "s" : 0,
        "t" : 0,
        "u" : 0,
        "v" : 0,
        "w" : 0,
        "x" : 0,
        "y" : 0,
        "z" : 0,
    }
    lowered_string = string.lower()
    for char in lowered_string:
        if char in chardict:   
            chardict[char] += 1
    return chardict


main()