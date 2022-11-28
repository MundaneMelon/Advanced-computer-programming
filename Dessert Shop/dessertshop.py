from desserts import *

def main():
    order = Order()

    order.add(Candy("Candy Corn", 1.5, .25))
    order.add(Candy("Gummy Bears", .25, .35))
    order.add(Cookie("Chocolate Chip", 6, 3.99))
    order.add(IceCream("Pistachio", 2, .79))
    order.add(Sundae("Vanilla", "Hot Fudge", 1.29))
    order.add(Cookie("Oatmeal Raisin", 2, 3.45))

    for i in order.order:
        print(i.name)
    print("Total number of items in order: " + str(order.item_count()))


if __name__ == '__main__':
    main()
