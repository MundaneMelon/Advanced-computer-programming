"""
Demonstrating
accessors/mutators
"""

from phone import *
from person import *

def main():
    my_phone = Phone("iPhone", 256, 12)
    print(my_phone.get_mode1())
    my_phone.set_model("Galaxy S20")
    print(my_phone.get_mode1())

    c = Person("Calvin")
    print(c.name)
    c.name = "Hobbes:"
    print(c.name)

if __name__ == "__main__":
    main()