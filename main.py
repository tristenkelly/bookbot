from stats import get_num_words
from stats import get_num_appearances
from stats import sort_on
import sys



def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

    
def main():
    filepath = sys.argv[1] if len(sys.argv) > 1 else print("Usage: python3 main.py <path_to_book>") or exit(1)
    book_text = get_book_text(filepath)
    num_words = get_num_words(filepath)
    appearances = get_num_appearances(filepath)
    print(f"Found {num_words} total words")
    print("Character appearances sorted by frequency:")
    values = [{"char":char, "num":num} for char, num in appearances.items()]
    values.sort(reverse=True, key=sort_on)
    for item in values:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

            



    
    
    
main()