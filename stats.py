def get_num_words(string_in):
    return len(string_in.split())

def get_num_chars(string_in):
    lwr = string_in.lower()
    dick = {}
    for char in lwr:
        if char in dick:
            dick[char] = dick[char] + 1
        else:
            dick[char] = 1
    return dick

def sort_on(items):
    return items["count"]

def get_sorted_list(dick):
    dlist = []
    for key in dick:
        temp = dict()
        temp["letter"] = key
        temp["count"] = dick[key]
        dlist.append(temp)
    dlist.sort(reverse=True, key=sort_on)
    return dlist
