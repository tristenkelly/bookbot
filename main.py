
def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content

def get_num_words(filepath):
    words = get_book_text(filepath).split()
    return len(words)
    
    
def main():
    filepath = "./books/frankenstein.txt"
    book_text = get_book_text(filepath)
    num_words = get_num_words(filepath)
    print(f"{num_words} words found in the document")
    
    
    
main()