def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count= length(file_contents)
        print(word_count)

def length(string):
    words = string.split()
    length = len(words)
    return length
        

main()