import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]  # the book path from command line
    book_text = get_book_text(path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    print("----------- Word Count ----------")
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    character_counts = count_characters(book_text)
    sorted_characters = sort_characters(character_counts)

    for item in sorted_characters:
        char = item["char"]
        num = item["num"]
        print(f"{char}: {num}")

    print("============= END ===============")

main()
