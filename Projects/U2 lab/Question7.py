def list_sum(list1):
    if len(list1) == 0:
        return 0
    return list1[0] + list_sum(list1[1:])