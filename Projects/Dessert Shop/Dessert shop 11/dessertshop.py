from desserts import *
from freeze import *

customer_db = dict[str]
def main():



    order = Order()
    main_menu(order)
    order.sort_items()

    user_input = input(
        '''
What is your name?
''')
    


    user_input = input(
        '''
 What would you like to add to the order? (1-4, Enter for done):
1: Cash
2: Card
3: Phone
Enter payment method:'''
    )
    if int(user_input) == 1:
        order.payment_method = PayType.CASH

    elif int(user_input) == 2:
        order.payment_method = PayType.CARD

    elif int(user_input) == 3:
        order.payment_method = PayType.PHONE
    print(order.__str__)

    dessertCustomer.add2history(order)
    user_input = input(
        '''
Would you like to make another order? [y/n]
'''
    )
    if (str(user_input) == 'y'):
        dessertCustomer.add2history(order)
        main()





def main_menu(order):
    print('''1: Candy
2: Cookie
3: Ice Cream
4: Sundae''')
    try:
        user_input = int(input('What would you like to add to the order? (1-4, Enter for done):'))
    except ValueError:
        pass
    print(" ")
    try:
        if user_input == 1:
            user_prompt_candy(order)
        elif user_input == 2:
            user_prompt_cookie(order)
        elif user_input == 3:
            user_prompt_icecream(order)
        elif user_input == 4:
            user_prompt_sundae(order)
    except UnboundLocalError:
        pass

def user_prompt_candy(order):
    name = input("Enter the type of candy:")
    weight = float(input("Enter the quantity of pounds you wish to purchase:"))
    price = float(input("Enter the price per pound:"))
    order.add(Candy(name, weight, price))
    main_menu(order)

def user_prompt_cookie(order):
    name = input("Enter the type of cookie:")
    qty = int(input("Enter the amount of cookies you wish to purchase:"))
    price = float(input("Enter the price per cookie:"))
    order.add(Cookie(name, qty, price))
    main_menu(order)

def user_prompt_icecream(order):
    name = input("Enter the name of the ice cream:")
    scoops = int(input("Enter the amount of scoops:"))
    price = float(input("Enter the price per scoop:"))
    order.add(IceCream(name, scoops, price))
    main_menu(order)

def user_prompt_sundae(order):
    name = input("Enter the name of the sundae:")
    topping = input("Enter the desired topping:")
    toppingPrice = float(input("Enter topping price:"))
    price = float(input('Enter the price per scoop:'))
    scoops = int(input('Enter the amount of scoops:'))
    order.add(Sundae(name, topping, toppingPrice, price, scoops))
    main_menu(order)


class Customer():
    def __init__(self, customer_name="Robert"):
        self._customer_name = customer_name
        self._customer_id = 3748327
        self.order_history = []

    @property
    def customer_id(self):
        return self._customer_id

    @customer_id.setter
    def customer_id(self, value):
        self._customer_id = value

    @property
    def customer_name(self):
        return self._customer_name

    @customer_name.setter
    def customer_name(self, value):
        self._customer_name = value

    def add2history(self, order):
        self.order_history.append(order)
        return self


# Stuff to do only once so running main again won't break anything
dessertCustomer = Customer()




if __name__ == '__main__':
    main()

