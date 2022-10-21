def recursive_power(int1, int2):
    if int2 == 0:
        return 1
    return int1 * recursive_power(int1, int2 - 1)
