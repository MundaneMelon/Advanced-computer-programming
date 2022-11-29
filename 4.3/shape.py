from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self._name = None
        self._area = 0.0

    def __str__(self):
        return "the shape " + self._name + \
            " has an area of " + str(self._area) \
            + " squared units."

    @property
    def name(self):
        return self._name

    @abstractmethod
    def calculate_area(self):
        pass