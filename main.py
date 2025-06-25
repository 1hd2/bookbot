from stats import get_num_words
from stats import get_num_chars
from stats import get_sorted_list
import sys

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    loc = sys.argv[1]
    words = get_book_text(loc)
    num_words = get_num_words(words)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {loc}...")
    num_chars = get_num_chars(words)
    slist = get_sorted_list(num_chars)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    for pair in slist:
        print(f'{pair["letter"]}: {pair["count"]}')
    print("============= END ===============")

main()
