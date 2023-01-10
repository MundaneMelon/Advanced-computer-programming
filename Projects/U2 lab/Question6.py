def recursive_sum(int1):
    if int1 == 0:
        return 0
    return int1 + recursive_sum(int1 - 1)