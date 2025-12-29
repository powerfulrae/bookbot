from stats import count_words
from stats import count_characters
from stats import sorted_chars
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    book = get_book_text(sys.argv[1])
    total_words = count_words(book)
    total_characters = count_characters(book)
    sorted_charnums = sorted_chars(total_characters)
    print(f"Found {total_words} total words")
    for dict in sorted_charnums:
        character = dict['char']
        count = dict['num']
        print(f'{character}: {count}')

main()

