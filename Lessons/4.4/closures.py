"""
This tutorial demonstrates the use of closures.
"""

def add_5():
    five = 5

    def add(arg):
        return arg + five
    return add

def main():
    closure = add_5()
    print(closure(1))
    print(closure(2))

if __name__ == '__main__':
    main()