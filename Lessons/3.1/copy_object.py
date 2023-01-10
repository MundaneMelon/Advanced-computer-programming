import copy

"""
This program demonstrates the use
of shallow and deep copies
"""

class ComicBookCharacter():
    pass

def main():
    a = ComicBookCharacter()
    a.name = "Calvin"
    a.age = 6
    a.type = "human"

    shallow_a = a
    deep_a = copy.deepcopy(a)
    a.name = "Hobbes"

    print(a.name)
    print(shallow_a.name)
    print(deep_a.name)

if __name__ == "__main__":
    main()