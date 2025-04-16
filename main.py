from stats import num_words, count_char, sort_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
        
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    number_of_words = num_words(text)
    char_dict = count_char(text)
    sorted_dict_list = sort_dict(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {number_of_words} total words")
    print("--------- Character Count -------")
    for el in sorted_dict_list:
        print(f"{el["key"]}: {el["val"]}")
    print("============= END ===============")
main()