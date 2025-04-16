from stats import num_words, count_char

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        
def main():
    text = get_book_text("books/frankenstein.txt")
    char_dict = count_char(text)
    print(f"{num_words(text)} words found in the document")
    print(char_dict)
    
main()