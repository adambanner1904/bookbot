from stats import get_num_words, create_sorted_list, get_char_count
import sys

# Escape program if used incorrectly
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()

text = get_book_text(path)

print(f"""

============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------
Found {get_num_words(text)} total words
--------- Character Count -------""")
for item in sorted(create_sorted_list(get_char_count(text)), key=lambda item: item['num'], reverse=True):
    if item['char'].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")
