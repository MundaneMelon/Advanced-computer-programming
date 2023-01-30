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

    #This shop makes absolutely no sense, so it's going to check for what kind of item it is rather than an item of a matching name
    #This way, The customer can still order whatever they want, and not be restrained to what's in the freezer.
    #It also means that any cookie in the freezer can become any type of cookie.
    #This may not work in real life, but it's what I'm going to do so I don't lose my mind
    def take(self, item: object):
        for i in self.items:
            if i == item.type:
                item.thaw()