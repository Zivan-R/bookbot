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

def sort_dict(dict):
    sorted_list = []
    
    for key, val in dict.items():
        if key.isalpha():
            tmp_dict = {"key": key, "val": val}
            sorted_list.append(tmp_dict)
    
    def sort_on(d):
        return d["val"]
    
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
        