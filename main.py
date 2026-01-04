import sys
from stats import count_words, count_letters, create_pretty

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    args = sys.argv

    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(args[1])
    print(f"Found {count_words(text)} total words")
    # print(count_letters(text))
    pretty_dict = create_pretty(count_letters(text))

    for line in pretty_dict:
        if line["char"].isalpha():
            print(f'{line["char"]}: {line["num"]}')
    
main()