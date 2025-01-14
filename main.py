with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    print(file_contents)

def count_words(file_contents):
    words = file_contents.split()
    count = len(words)
    print(count)

def count_characters(file_contents):
    characters = {}
    for char in file_contents:
        char = char.lower()
        characters[char] = characters.get(char, 0) + 1
    print(characters)

count_words(file_contents)
count_characters(file_contents)