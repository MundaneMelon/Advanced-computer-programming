def search_list(list1, search):
    for i in range(len(list1)):
        if list1[i].lower() == search.lower():
            return i
    return -1