from abc import ABC, abstractmethod
from enum import Enum
from freeze import *
from payment import *
import combine


class DessertItem(ABC):
    def __init__(self, name="", tax_percent=7.25):
        self._name = name
        self._tax_percent = tax_percent
        self._packaging = None

    @property
    def packaging(self):
        return self._packaging

    @packaging.setter
    def packaging(self, new_packaging):
        self._packaging = new_packaging

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def tax_percent(self):
        return self._tax_percent

    @tax_percent.setter
    def tax_percent(self, tax_percent):
        self._tax_percent = tax_percent

    @abstractmethod
    def calculate_cost(self):
        pass

    def calculate_tax(self):
        return self.calculate_cost() * (self.tax_percent * .01)

    def __eq__(self, other):
        return self.calculate_cost() == other.calculate_cost()

    def __lt__(self, other):
        return self.calculate_cost() < other.calculate_cost()

    def __gt__(self, other):
        return self.calculate_cost() > other.calculate_cost()

    def __ge__(self, other):
        return self.calculate_cost() >= other.calculate_cost()

    def __le__(self, other):
        return self.calculate_cost() <= other.calculate_cost()


class Candy(DessertItem):
    def __init__(self, name='', candy_weight=5.5, price_per_pound=2.75,
tax_percent=7.25):
        super().__init__(name, tax_percent)
        self._name = name
        self._candy_weight = candy_weight
        self._price_per_pound = price_per_pound
        self._tax_percent = tax_percent
        self.packaging = "Bag"
        self.type = "Candy"

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

    @property
    def __str__(self):
        result = f"     {self.candy_weight}lbs @ ${self.price_per_pound}/lb:"
        result = f"{find_spaces(result, 30)}${self.calculate_cost():.2f}"
        result = f"{find_spaces(result, 40)}[Tax:${self.calculate_tax():.2f}]"
        return f"{self.name} ({self.packaging})\n{result}"
        # Find spaces is a function I wrote to make this easier. It's at the bottom

    def can_combine(self, other:"Candy"):
        if self.type == other.type:
            if self.name == other.name and \
                self.price_per_pound == other.price_per_pound:
                return True
        else:
            return False
    def combine(self, other: "Candy") -> "Candy":
        if self.can_combine(other):
            self.candy_weight += other.candy_weight


class Cookie(DessertItem):
    def __init__(self, name='', cookieQty=10, pricePerDozen=12.5,
tax_percent=7.25):
        super().__init__(name, tax_percent)
        self._name = name
        self._cookieQty = cookieQty
        self._pricePerDozen = pricePerDozen
        self._tax_percent = tax_percent
        self.packaging = "Box"
        self._temperature = "thawing"
        self.type = "Cookie"

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

    # Freeze implementation
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def chill(self):
        self.temperature = "chilling"

    def thaw(self):
        self.temperature = "thawing"

    @property
    def __str__(self):
        result = f"     {self.cookieQty} @ ${self.pricePerDozen}/cookie:"
        result = f"{find_spaces(result, 30)}${self.calculate_cost():.2f}"
        result = f"{find_spaces(result, 40)}[Tax:${self.calculate_tax():.2f}]"
        return f"{self.name} ({self.packaging})\n{result}"

    def can_combine(self, other:"Cookie"):
        if self.type == other.type:
            if self.name == other.name and \
                self.pricePerDozen == other.pricePerDozen:
                return True
        else:
            return False

    def combine(self, other:"Cookie") -> "Cookie":
        if self.can_combine(other):
                self.cookieQty += other.cookieQty


class IceCream(DessertItem):
    def __init__(self, name='', scoopCount=5, pricePerScoop=2.75, tax_percent=7.25):
        super().__init__(name, tax_percent)
        self._name = name
        self._scoopCount = scoopCount
        self._pricePerScoop = pricePerScoop
        self._tax_percent = tax_percent
        self.packaging = "Bowl"
        self.type = "IceCream"

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

    # Freeze implementation
    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value
    def chill(self):
        self.temperature = "chilling"
    def thaw(self):
        self.temperature = "thawing"

    @property
    def __str__(self):
        result = f"     {self.scoopCount} @ ${self.pricePerScoop}/scoop:"
        result = f"{find_spaces(result, 30)}${self.calculate_cost():.2f}"
        result = f"{find_spaces(result, 40)}[Tax:${self.calculate_tax():.2f}]"
        return f"{self.name} ({self.packaging})\n{result}"


class Sundae(IceCream):
    def __init__(self, name='', toppingName='Marshmallows', \
                 toppingPrice=2.25, pricePerScoop=2.75, scoopCount=5,
tax_percent=7.25):
        super().__init__(name, tax_percent)
        self.name = name
        self._toppingName = toppingName
        self._toppingPrice = toppingPrice
        self._tax_percent = tax_percent
        self._pricePerScoop = pricePerScoop
        self._scoopCount = scoopCount
        self.packaging = "Boat"
        self.type = "Sundae"

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

    @property
    def __str__(self):
        result = f"     {self.toppingName} @ ${self.toppingPrice}:"
        result = f"{find_spaces(result, 30)}${self.calculate_cost():.2f}"
        result = f"{find_spaces(result, 40)}[Tax:${self.calculate_tax():.2f}]"
        return f"{self.name} ({self.packaging})\n     {self.scoopCount} scoops @ ${self.pricePerScoop}\n{result}"


class Order():
    def __init__(self, order=[], payment_method = PayType.CASH):
        self._order = order
        self._payment_method = payment_method

    @property
    def order(self):
        return self._order

    @order.setter
    def order(self, value):
        self._order = value


    @property
    def payment_method(self):
        return self._payment_method

    @payment_method.setter
    def payment_method(self, value):
        self._payment_method = value

    @property
    def order(self):
        return self._order

    def add(self, listItem):
        check = False
        for i in self.order:
            if (i.type == "Candy" and listItem.type == "Candy") or (listItem.type == "Cookie" and i.type == "Cookie"):
                if i.can_combine(listItem):
                    i.combine(listItem)
                    check = True
                    listItem.type = None
        if not check:
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

    def sort_items(self):
        self.order.sort()

    @property
    def __str__(self):
        result = '------------Receipt---------------\n'
        for i in self.order:
            result += f"{i.__str__}\n"
        result += '------------------------------------------------------\n'
        result += f"Total items in the order: {self.item_count()}\n"
        result2 = f"Order Subtotals:|         ${self.order_cost():.2f}"
        result += f"{find_spaces(result2, 40)}[Tax: ${self.order_tax():.2f}]\n"
        result3 = f"Order Total:"
        result += f"{find_spaces(result3, 40)}${self.order_tax() + self.order_cost():.2f}"
        return f"{result}\n------------------------------------------------------\n\Paid with {self.payment_method.name}"

# def find_spaces(str, space):
#     spaces = space - len(str)
#     if spaces > 0:
#         str += " " * spaces
#     else:
#         str += " "
#     return str

def find_spaces(str, column):
    if len(str) >= column:
        return ''
    else:
        return str + (" " * (column - len(str)))

