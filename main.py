def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
def main():
    get_book_text("books/frankenstein.txt")
    
main()