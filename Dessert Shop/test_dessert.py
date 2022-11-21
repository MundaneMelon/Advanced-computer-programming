from desserts import *

def inc(x):
    return x + 1


def test_DessertItem():
    dessert = DessertItem()
    assert dessert.name == ""
    dessert2 = DessertItem('Brownie')
    assert dessert2.name == 'Brownie'

    dessert.name = 'Cake'
    assert dessert.name == 'Cake'
    dessert2.name = 'Cake'
    assert dessert2.name == 'Cake'


def test_Candy():
    candy = Candy()
    assert candy.candy_weight == 5.5
    assert candy.price_per_pound == 25.75
    assert candy.name == ''
    candy2 = Candy(10, 2.75, 'Twix')
    assert candy2.candy_weight == 10
    assert candy2.price_per_pound == 2.75
    assert candy2.name == 'Twix'

    candy.candy_weight = 1000
    assert candy.candy_weight == 1000
    candy.price_per_pound = 2000
    assert candy.price_per_pound == 2000
    candy.name = 'Yummy stuff'
    assert candy.name == 'Yummy stuff'

    candy2.candy_weight = 1000
    assert candy2.candy_weight == 1000
    candy2.price_per_pound = 2000
    assert candy2.price_per_pound == 2000
    candy2.name = 'Yummy stuff'
    assert candy2.name == 'Yummy stuff'



def test_Cookie():
    cookie = Cookie()
    assert cookie.cookieQty == 10
    assert cookie.pricePerDozen == 12.5
    assert cookie.name == ''
    cookie2 = Cookie(15, 20.5, 'Chocolate Chip')
    assert cookie2.cookieQty == 15
    assert cookie2.pricePerDozen == 20.5
    assert cookie2.name == 'Chocolate Chip'

    cookie.cookieQty = 1
    assert cookie.cookieQty == 1
    cookie.pricePerDozen = 2
    assert cookie.pricePerDozen == 2
    cookie.name = 'thing'
    assert cookie.name == 'thing'

    cookie2.cookieQty = 1
    assert cookie2.cookieQty == 1
    cookie2.pricePerDozen = 2
    assert cookie2.pricePerDozen == 2
    cookie2.name = 'thing'
    assert cookie2.name == 'thing'

def test_IceCream():
    cream = IceCream()
    assert cream.scoopCount == 5
    assert cream.pricePerScoop == 2.75
    assert cream.name == ''
    cream2 = IceCream(10, 5, 'Chocolate')
    assert cream2.scoopCount == 10
    assert cream2.pricePerScoop == 5
    assert cream2.name == 'Chocolate'

    cream.scoopCount = 200
    assert cream.scoopCount == 200
    cream.pricePerScoop = 500
    assert cream.pricePerScoop == 500
    cream.name = 'CREEEEEAAAAAMMMM'
    assert cream.name == 'CREEEEEAAAAAMMMM'

    cream2.scoopCount = 200
    assert cream2.scoopCount == 200
    cream2.pricePerScoop = 500
    assert cream2.pricePerScoop == 500
    cream2.name = 'CREEEEEAAAAAMMMM'
    assert cream2.name == 'CREEEEEAAAAAMMMM'

def test_Sundae():
    sundae = Sundae()
    assert sundae.toppingName == 'Marshmellows'
    assert sundae.toppingPrice == 2.25
    assert sundae.name == ''
    sundae2 = Sundae('Whipped Cream', 5, 'Banana Split')
    assert sundae2.toppingName == 'Whipped Cream'
    assert sundae2.toppingPrice == 5
    assert sundae2.name == 'Banana Split'

    sundae.toppingName = 'Caramel'
    assert sundae.toppingName == 'Caramel'
    sundae.toppingPrice = 999
    assert sundae.toppingPrice == 999
    sundae.name = 'Chocolate surprise'
    assert sundae.name == 'Chocolate surprise'

    sundae2.toppingName = 'Caramel'
    assert sundae2.toppingName == 'Caramel'
    sundae2.toppingPrice = 999
    assert sundae2.toppingPrice == 999
    sundae2.name = 'Chocolate surprise'
    assert sundae2.name == 'Chocolate surprise'


