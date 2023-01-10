"""
This tutorial demonstrates a function as a return vale
"""

# normal function which returns data
def add_two_nums(x, y):
    return x + y

# normal function which returns data
def add_three_nums(x, y, z):
    return x + y + z

# function which returns functions depending on the logic
def get_appropriate_function(num_len):
    if num_len == 3:
        return add_three_nums
    else:
        return add_two_nums

def main():
    args = [1, 2, 3]
    num_len = len(args)
    res_function = get_appropriate_function(num_len)
    print(res_function)
    print(res_function(*args))  # unpack the args, output 6

    args = [1, 2]
    num_len = len(args)
    res_function = get_appropriate_function(num_len)
    print(res_function)
    print(res_function(*args)) # unpack the args, output 3

if __name__ == "__main__":
    main()