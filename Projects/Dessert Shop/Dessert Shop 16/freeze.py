from typing import Protocol
from desserts import *

class Freeze(Protocol):
    def __init__(self):
        self._temperature = None
    @property
    def temperature(self):
        pass
    @temperature.setter
    def temperature(self, value):
        pass
    def chill(self):
        pass
    def thaw(self):
        pass
class Freezer():
    def __init__(self):
        self._items = []
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value
    def put(self, item: Freeze):
        self.items.append(item)
        item.chill()
    def take(self, item: object):
        for i in self.items:
            if i == item.type:
                item.thaw()
