from desserts import *
from freeze import *
from customer import *

global customer_db
customer_db = {}
global customer_id
customer_id = 999
def main():

    order = Order([])
    main_menu(order)
    order.sort_items()

    customer_name = input(
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

    check = False
    for i in customer_db:
        if i == customer_name:
            check = True

    if not check:
        customer_db[customer_name] = Customer(customer_name)
        global customer_id
        customer_id += 1
        customer_db[customer_name].customer_id = customer_id

    customer_db[customer_name].order_history.append(order)
    customer_db[customer_name].total_orders += 1




    print(f"Customer Name: {customer_name}       Customer ID: {customer_id}    \
      Total Orders: {customer_db[customer_name].total_orders}")
    user_input = input(
        '''
Press y and enter to start a new order
'''
    )
    if (str(user_input) == 'y'):
        main()





def main_menu(order):
    print('''1: Candy
2: Cookie
3: Ice Cream
4: Sundae
5: Admin Module''')
    try:
        user_input = int(input('What would you like to add to the order? (1-5, Enter for done):'))
    except ValueError:
        pass
    try:
        if user_input == 1:
            user_prompt_candy(order)
        elif user_input == 2:
            user_prompt_cookie(order)
        elif user_input == 3:
            user_prompt_icecream(order)
        elif user_input == 4:
            user_prompt_sundae(order)
        elif user_input == 5:
            admin.admin_menu(order)
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


# class Customer():
#     def __init__(self, customer_name="Robert"):
#         self._customer_name = customer_name
#         self._customer_id = 3748327
#         self.order_history = []
#
#     @property
#     def customer_id(self):
#         return self._customer_id
#
#     @customer_id.setter
#     def customer_id(self, value):
#         self._customer_id = value
#
#     @property
#     def customer_name(self):
#         return self._customer_name
#
#     @customer_name.setter
#     def customer_name(self, value):
#         self._customer_name = value
#
#     def add2history(self, order):
#         self.order_history.append(order)
#         return self
#

# Stuff to do only once so running main again won't break anything
dessertCustomer = Customer()

class admin():
    def admin_menu(order):
        user_input = int(input(
            '''
1: Shop Customer List
2: Customer Order History
3: Best Customer
4: Exit Admin Module
'''
        ))
        try:
            if user_input == 1:
                admin.shop_customer_list(order)
            elif user_input == 2:
                user_input = input("Customer's name: ")
                admin.customer_order_history(order, user_input)
            elif user_input == 3:
                admin.best_customer(order)
            elif user_input == 4:
                main_menu(order)
        except UnboundLocalError:
            pass

    def shop_customer_list(order):
        for i in customer_db:
            print(f"Customer Name: {customer_db[i].customer_name}     \
                 Customer ID:{customer_db[i].customer_id}")
        admin.admin_menu(order)

    def customer_order_history(order, name):
        customer_check = False
        for i in customer_db:
            if name == i:
                customer_check = True
        if customer_check:
            for f in customer_db[i].order_history:
                print(f.__str__)
        else:
            print("Could not find any customer with that name")
        admin.admin_menu(order)

    def best_customer(order):
        if len(customer_db) == 0:
            print("There are not customers yet")
        else:
            best_customer = None
            for i in customer_db:
                if best_customer == None:
                    best_customer = i
                else:
                    if customer_db[i].total_orders > customer_db[best_customer].total_orders:
                        best_customer = i
            print(f'''
------------------------------------------------------------------------
The best customer is {best_customer}
------------------------------------------------------------------------
                ''')
        admin.admin_menu(order)



if __name__ == '__main__':
    main()

