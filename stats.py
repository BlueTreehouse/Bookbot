def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    count_dict = {}
    lower_count = text.lower()
    for char in lower_count:
        if char not in count_dict:
            count_dict.update({char:1})
        else:
            count_dict.update({char:(count_dict.get(char) + 1)})
    return count_dict

def sort_on(d):
    return d["num"]

def sort_count(dictionary):
    sort_list = []
    for i in dictionary:
        sort_list.append({"char": i, "num": dictionary[i]})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list