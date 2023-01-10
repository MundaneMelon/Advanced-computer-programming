class Person:
    def __init__(self, name,age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation

    def say_hello(self):
        print(f"Hello, my name is " f"(self.name).")

    def say_age(self):
        print(f"I am {self.age} years old.")
