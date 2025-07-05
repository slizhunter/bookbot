import sys
from stats import count_words, count_chars, sorted_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
def print_book_stats(book_path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = count_words(get_book_text(book_path))
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_word_list = sorted_dict(count_chars(get_book_text(book_path)))
    for item in sorted_word_list:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print_book_stats(sys.argv[1])

main()