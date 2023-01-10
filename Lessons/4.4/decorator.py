"""
This tutorial demonstrates the use of decorators
"""


def say_it_twice(func):
    def wrapper_say_it_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_say_it_twice

@say_it_twice
def say_whee():
    print("Whee!")

@say_it_twice
def greet(name):
    print(f"Hello {name}!")
    
say_whee()
greet("World")