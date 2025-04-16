def num_words(text):
    text_list = text.split()
    return len(text_list)

def count_char(text):
    ltext = text.lower()
    char_dict = dict()
    
    for i in range(len(ltext)):
        if ltext[i] not in char_dict.keys():
            char_dict[ltext[i]] = 1
        else:
            char_dict[ltext[i]] += 1
    
    return char_dict