from stats import get_num_words, char_count, sort_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dictionary = char_count(text)
    sort = sort_count(dictionary)
    print_report(book_path, num_words, sort)
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_report(book_path, num_words, sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()
