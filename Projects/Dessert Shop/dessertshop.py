from desserts import *
from freeze import *

def main():


    order = Order()
    main_menu(order)
    print(order.__str__)

    # print("\n" + " " * 13 + 'Receipt')
    #
    # for i in order.order:
    #     result = find_spaces(i.name)
    #     if i.calculate_cost() < 10:
    #         result += " "
    #
    #     result += "$" + str(round(i.calculate_cost(), 2)) + " [Tax: $" + str(round(i.calculate_tax(), 2)) + "]"
    #     print(result)
    # print("-" * 30)


    # print(find_spaces("Order Subtotals:", 30) + " $" + str(round(order.order_cost(), 2)) + '[Tax:$' + str(round(order.order_tax(), 2)) + ']')
    # print(find_spaces("Order Total:", 30) + " $" + str(round((order.order_cost() + order.order_tax()), 2)))
    # print(find_spaces("Total items in the order:", 30) + " " + str(order.item_count()))





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

if __name__ == '__main__':
    main()
