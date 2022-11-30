from abc import ABC, abstractmethod

class DessertItem(ABC):

    def __init__(self, name="", tax_percent=7.25):
        self._name = name
        self._tax_percent = tax_percent

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tax_percent(self):
        return self._tax_percent

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent * .01)



class Candy(DessertItem):
    def __init__(self, name='', candy_weight=5.5, price_per_pound=2.75, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self._name = name
        self._candy_weight = candy_weight
        self._price_per_pound = price_per_pound
        self._tax_percent = tax_percent


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

    def calculate_cost(self):
        return self.candy_weight * self.price_per_pound

class Cookie(DessertItem):
    def __init__(self, name='', cookieQty=10, pricePerDozen=12.5, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self._name = name
        self._cookieQty = cookieQty
        self._pricePerDozen = pricePerDozen
        self._tax_percent = tax_percent

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

    def calculate_cost(self):
        return self.cookieQty * self.pricePerDozen

class IceCream(DessertItem):
    def __init__(self, name='', scoopCount=5, pricePerScoop=2.75, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self._name = name
        self._scoopCount = scoopCount
        self._pricePerScoop = pricePerScoop
        self._tax_percent = tax_percent

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

    def calculate_cost(self):
        return self.scoopCount * self.pricePerScoop


class Sundae(IceCream):
    def __init__(self, name='', toppingName='Marshmellows', \
                 toppingPrice=2.25, pricePerScoop=2.75, scoopCount=5, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self.name = name
        self._toppingName = toppingName
        self._toppingPrice = toppingPrice
        self._tax_percent = tax_percent
        self._pricePerScoop = pricePerScoop
        self._scoopCount = scoopCount

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

    def calculate_cost(self):
        return (self.scoopCount * self.pricePerScoop) + self.toppingPrice


class Order():
    def __init__(self, order=[]):
        self._order = order

    @property
    def order(self):
        return self._order

    def add(self, listItem):
        self.order.append(listItem)

    def item_count(self):
        return len(self.order)

    def order_cost(self):
        result = 0
        for i in self.order:
            result += i.calculate_cost()
        return result

    def order_tax(self):
        result = 0
        for i in self.order:
            result += i.calculate_tax()
        return result


