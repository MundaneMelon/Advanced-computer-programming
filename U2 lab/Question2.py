def odds_or_evens(condition, list1):
    list2 = []
    for i in list1:
        if i % 2 == 0 and condition:
            list2.append(i)
        if i % 2 != 0 and not condition:
            list2.append(i)
    print(list2)