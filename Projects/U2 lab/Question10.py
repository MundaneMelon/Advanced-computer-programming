def get_max(list):
    largest = list[0]
    for i in list:
        if i > largest:
            largest = i
    return largest
