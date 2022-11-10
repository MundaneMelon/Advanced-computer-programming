"""
Definition of
Vehicle class
"""


class Vehicle:
    def __init__(self, make, model):
        self._make = make
        self._model = model

    def get_make(self):
        return self._make

    def set_make(self, new_make):
        self._make = new_make

    make = property(get_make, set_make)