def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def num_words(text):
    text_list = text.split()
    return len(text_list)
        
def main():
    text = get_book_text("books/frankenstein.txt")
    print(f"{num_words(text)} words found in the document")
    
main()