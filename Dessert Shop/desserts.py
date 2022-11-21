class DessertItem:

    def __init__(self, name=""):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name



class Candy(DessertItem):
    def __init__(self, candy_weight=5.5, price_per_pound=25.75, name=''):
        self.name = name
        self._candy_weight = candy_weight
        self._price_per_pound = price_per_pound

    @property
    def candy_weight(self):
        return self._candy_weight

    @candy_weight.setter
    def candy_weight(self, weight):
        self._candy_weight = weight

    @property
    def price_per_pound(self):
        return self._price_per_pound

    @price_per_pound.setter
    def price_per_pound(self, price):
        self._price_per_pound = price

class Cookie(DessertItem):
    def __init__(self, cookieQty=10, pricePerDozen=12.5, name=""):
        self.name = name
        self._cookieQty = cookieQty
        self._pricePerDozen = pricePerDozen

    @property
    def cookieQty(self):
        return self._cookieQty

    @cookieQty.setter
    def cookieQty(self, cookie):
        self._cookieQty = cookie

    @property
    def pricePerDozen(self):
        return self._pricePerDozen

    @pricePerDozen.setter
    def pricePerDozen(self, price):
        self._pricePerDozen = price

class IceCream(DessertItem):
    def __init__(self, scoopCount=5, pricePerScoop=2.75, name=""):
        self.name = name
        self._scoopCount = scoopCount
        self._pricePerScoop = pricePerScoop

    @property
    def scoopCount(self):
        return self._scoopCount

    @scoopCount.setter
    def scoopCount(self, scoops):
        self._scoopCount = scoops

    @property
    def pricePerScoop(self):
        return self._pricePerScoop

    @pricePerScoop.setter
    def pricePerScoop(self, price):
        self._pricePerScoop = price


class Sundae(IceCream):
    def __init__(self, toppingName='Marshmellows', toppingPrice=2.25, name=""):
        self.name = name
        self._toppingName = toppingName
        self._toppingPrice = toppingPrice

    @property
    def toppingName(self):
        return self._toppingName

    @toppingName.setter
    def toppingName(self, name):
        self._toppingName = name

    @property
    def toppingPrice(self):
        return self._toppingPrice

    @toppingPrice.setter
    def toppingPrice(self, price):
        self._toppingPrice = price

class Order(DessertItem):
    pass




