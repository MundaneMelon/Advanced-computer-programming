from desserts import *


def test_Candy():
    candy = Candy()
    assert candy.candy_weight == 5.5
    assert candy.price_per_pound == 2.75
    assert candy.name == ''
    assert candy.tax_percent == 7.25
    candy2 = Candy('Twix', 10, 2.75, 50)
    assert candy2.candy_weight == 10
    assert candy2.price_per_pound == 2.75
    assert candy2.name == 'Twix'
    assert candy2.tax_percent == 50


    #There's no way I'm making a test case for all 4 variations of each class object.
    #one is plenty
    assert candy.calculate_cost() == 15.125
    assert candy.calculate_tax() == 1.0965624999999999



    candy.candy_weight = 1000
    assert candy.candy_weight == 1000
    candy.price_per_pound = 2000
    assert candy.price_per_pound == 2000
    candy.name = 'Yummy stuff'
    assert candy.name == 'Yummy stuff'
    candy.tax_percent = 25
    assert candy.tax_percent == 25

    candy2.candy_weight = 1000
    assert candy2.candy_weight == 1000
    candy2.price_per_pound = 2000
    assert candy2.price_per_pound == 2000
    candy2.name = 'Yummy stuff'
    assert candy2.name == 'Yummy stuff'
    candy2.tax_percent = 75
    assert candy2.tax_percent == 75


def test_Cookie():
    cookie = Cookie()
    assert cookie.cookieQty == 10
    assert cookie.pricePerDozen == 12.5
    assert cookie.name == ''
    assert cookie.tax_percent == 7.25
    cookie2 = Cookie('Chocolate Chip', 15, 20.5, 50)
    assert cookie2.cookieQty == 15
    assert cookie2.pricePerDozen == 20.5
    assert cookie2.name == 'Chocolate Chip'
    assert cookie2.tax_percent == 50


    assert cookie.calculate_cost() == 125
    assert cookie.calculate_tax() == 9.0625

    cookie.cookieQty = 1
    assert cookie.cookieQty == 1
    cookie.pricePerDozen = 2
    assert cookie.pricePerDozen == 2
    cookie.name = 'thing'
    assert cookie.name == 'thing'
    cookie.tax_percent = 75
    assert cookie.tax_percent == 75

    cookie2.cookieQty = 1
    assert cookie2.cookieQty == 1
    cookie2.pricePerDozen = 2
    assert cookie2.pricePerDozen == 2
    cookie2.name = 'thing'
    assert cookie2.name == 'thing'
    cookie2.tax_percent = 25
    assert cookie2.tax_percent == 25


def test_IceCream():
    cream = IceCream()
    assert cream.scoopCount == 5
    assert cream.pricePerScoop == 2.75
    assert cream.name == ''
    assert cream.tax_percent == 7.25
    cream2 = IceCream('Chocolate', 10, 5, 50)
    assert cream2.scoopCount == 10
    assert cream2.pricePerScoop == 5
    assert cream2.name == 'Chocolate'
    assert cream2.tax_percent == 50

    assert cream.calculate_cost() == 13.75
    assert cream.calculate_tax() == .996875

    cream.scoopCount = 200
    assert cream.scoopCount == 200
    cream.pricePerScoop = 500
    assert cream.pricePerScoop == 500
    cream.name = 'CREEEEEAAAAAMMMM'
    assert cream.name == 'CREEEEEAAAAAMMMM'
    cream.tax_percent = 75
    assert cream.tax_percent == 75

    cream2.scoopCount = 200
    assert cream2.scoopCount == 200
    cream2.pricePerScoop = 500
    assert cream2.pricePerScoop == 500
    cream2.name = 'CREEEEEAAAAAMMMM'
    assert cream2.name == 'CREEEEEAAAAAMMMM'
    cream2.tax_percent = 25
    assert cream2.tax_percent == 25

def test_Sundae():
    sundae = Sundae()
    assert sundae.toppingName == 'Marshmallows'
    assert sundae.toppingPrice == 2.25
    assert sundae.name == ''
    assert sundae.tax_percent == 7.25
    assert sundae.pricePerScoop == 2.75
    assert sundae.scoopCount == 5
    sundae2 = Sundae('Banana Split', 'Whipped Cream', 5, 1.75, 2, 50)
    assert sundae2.toppingName == 'Whipped Cream'
    assert sundae2.toppingPrice == 5
    assert sundae2.name == 'Banana Split'
    assert sundae2.tax_percent == 50
    assert sundae2.scoopCount == 2
    assert sundae2.pricePerScoop == 1.75

    assert sundae.calculate_cost() == 16
    assert sundae.calculate_tax() == 1.16

    sundae.toppingName = 'Caramel'
    assert sundae.toppingName == 'Caramel'
    sundae.toppingPrice = 999
    assert sundae.toppingPrice == 999
    sundae.name = 'Chocolate surprise'
    assert sundae.name == 'Chocolate surprise'
    sundae.scoopCount = 10
    assert sundae.scoopCount == 10
    sundae.pricePerScoop = 10.50
    assert sundae.pricePerScoop == 10.50
    sundae.tax_percent = 75
    assert sundae.tax_percent == 75

    sundae2.toppingName = 'Caramel'
    assert sundae2.toppingName == 'Caramel'
    sundae2.toppingPrice = 999
    assert sundae2.toppingPrice == 999
    sundae2.name = 'Chocolate surprise'
    assert sundae2.name == 'Chocolate surprise'

    sundae2.scoopCount = 1
    assert sundae2.scoopCount == 1
    sundae2.pricePerScoop = 1.50
    assert sundae2.pricePerScoop == 1.5
    sundae2.tax_percent = 25
    assert sundae2.tax_percent == 25

def test_payment():
    order = Order()
    assert order.payment_method.name == "CASH"

    order.payment_method = PayType.CARD
    assert order.payment_method.name == "CARD"