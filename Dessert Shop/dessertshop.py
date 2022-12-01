from desserts import *

def main():
    order = Order()

    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 3, 1.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.99))

    print("\n" + " " * 13 + 'Receipt')

    for i in order.order:
        result = find_spaces(i.name)
        if i.calculate_cost() < 10:
            result += " "

        result += "$" + str(round(i.calculate_cost(), 2)) + "[Tax: $" + str(round(i.calculate_tax(), 2)) + "]"
        print(result)
    print("-" * 30)
    print(find_spaces("Order Subtotals:") + " $" + str(round(order.order_cost(), 2)) + '[Tax:$' + str(round(order.order_tax(), 2)) + ']')
    print(find_spaces("Order Total:") + " $" + str(round((order.order_cost() + order.order_tax()), 2)))
    print(find_spaces("Total items in the order:") + " " + str(order.item_count()))


def find_spaces(str):
    spaces = 30 - len(str)
    str += " " * spaces
    return str

if __name__ == '__main__':
    main()
