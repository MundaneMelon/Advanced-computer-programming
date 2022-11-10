"""
Definition of
the Person class
"""

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as \
                            a string")
        self._name = new_name