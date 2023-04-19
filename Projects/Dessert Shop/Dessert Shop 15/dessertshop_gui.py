import sys
from desserts import *
from customer import *
import tkinter

global customer_db
customer_db = {}
global customer_id
customer_id = 999


def gui_main():
    order = Order([])
    window = tkinter.Tk()
    window.title("Dessert Shop")
    window.geometry("300x200")
    window.configure(background="#d9d9d9")
    screen1(window, order)


def screen1(window, order):
    refresh(window)
    l = tkinter.Label(window, text="What would you like to add to the order?")
    l.config(font=("Courier", 9))
    l.pack()
    tkinter.Button(window, text="Candy", command=lambda: candy_screen(window, order)).pack()
    tkinter.Button(window, text="Cookie", command=lambda: cookie_screen(window, order)).pack()
    tkinter.Button(window, text="Ice Cream", command=lambda: icecream_screen(window, order)).pack()
    tkinter.Button(window, text="Sundae", command=lambda: sundae_screen(window, order)).pack()
    tkinter.Button(window, text="Done with order", command=lambda: final_details_screen(window, order)).pack()
    window.mainloop()


def candy_screen(window, order):
    refresh(window)
    l1 = tkinter.Label(window, text="What type of candy would you like to order?").pack()
    i1 = tkinter.Entry(window, width=35)
    i1.pack()
    l2 = tkinter.Label(window, text="How many pounds would you like to buy?").pack()
    i2 = tkinter.Entry(window, width=17)
    i2.pack()
    l3 = tkinter.Label(window, text="What is the price per pound?").pack()
    i3 = tkinter.Entry(window, width=17)
    i3.pack()
    b1 = tkinter.Button(window, text="Add to order", command=lambda: \
        add_order(window, order, 'Candy', i1.get(), i2.get(), i3.get(), 0, 0)).pack()
    b2 = tkinter.Button(window, text="I want to go back :(", command=lambda: screen1(window, order)).pack()
    window.mainloop()


def cookie_screen(window, order):
    refresh(window)
    l1 = tkinter.Label(window, text="What type of cookie would you like to order?").pack()
    i1 = tkinter.Entry(window, width=35)
    i1.pack()
    l2 = tkinter.Label(window, text="How many cookies would you like to buy?").pack()
    i2 = tkinter.Entry(window, width=17)
    i2.pack()
    l3 = tkinter.Label(window, text="What is the price per cookie?").pack()
    i3 = tkinter.Entry(window, width=17)
    i3.pack()
    b1 = tkinter.Button(window, text="Add to order", command=lambda: \
        add_order(window, order, 'Cookie', i1.get(), i2.get(), i3.get(), 0, 0)).pack()
    b2 = tkinter.Button(window, text="I want to go back :(", command=lambda: screen1(window, order)).pack()
    window.mainloop()


def sundae_screen(window, order):
    refresh(window)
    window.geometry('300x300')
    tkinter.Label(window, text="What type of ice cream would you like to order?").pack()
    i1 = tkinter.Entry(window, width=35)
    i1.pack()
    tkinter.Label(window, text="How many scoops do you want?").pack()
    i2 = tkinter.Entry(window, width=17)
    i2.pack()
    tkinter.Label(window, text="What is the price per scoop?").pack()
    i3 = tkinter.Entry(window, width=17)
    i3.pack()
    l4 = tkinter.Label(window, text="What is the name of the topping?").pack()
    i4 = tkinter.Entry(window, width=35)
    i4.pack()
    tkinter.Label(window, text="What is the price of the topping?").pack()
    i5 = tkinter.Entry(window, width=17)
    i5.pack()
    tkinter.Button(window, text="Add to order", command=lambda: \
        add_order(window, order, 'Candy', i1.get(), i2.get(), i3.get(), 0, 0)).pack()
    tkinter.Button(window, text="I want to go back :(", command=lambda: screen1(window, order)).pack()
    window.mainloop()


def icecream_screen(window, order):
    refresh(window)
    tkinter.Label(window, text="What type of ice cream would you like to order?").pack()
    i1 = tkinter.Entry(window, width=35)
    i1.pack()
    tkinter.Label(window, text="How many scoops would you like to purchase?").pack()
    i2 = tkinter.Entry(window, width=17)
    i2.pack()
    tkinter.Label(window, text="What is the price per scoop?").pack()
    i3 = tkinter.Entry(window, width=17)
    i3.pack()
    tkinter.Button(window, text="Add to order", command=lambda: \
        add_order(window, order, 'IceCream', i1.get(), i2.get(), i3.get(), 0, 0)).pack()
    tkinter.Button(window, text="I want to go back :(", command=lambda: screen1(window, order)).pack()
    window.mainloop()


def add_order(window, order, dessert, name, weight, price, topping, toppingprice):
    try:
        if dessert == 'Candy':
            order.add(Candy(name, float(weight), float(price)))
        elif dessert == 'Cookie':
            order.add(Cookie(name, int(weight), float(price)))
        elif dessert == 'IceCream':
            order.add(IceCream(name, int(weight), float(price)))
        elif dessert == 'Sundae':
            order.add(Sundae(name, topping, float(toppingprice), float(price), int(weight)))
            window.geometry("300x200")
        else:
            print("Something wacky is going on man")
    except ValueError:
        error_screen(window, order)
    screen1(window, order)


def error_screen(window, order):
    refresh(window)
    window.geometry("300x200")
    l1 = tkinter.Label(window, text="Value error, make sure inputs are correct").place(x=40, y=80)
    b1 = tkinter.Button(window, text="Take me back", command=lambda: screen1(window, order)).place(x=110, y=170)
    window.mainloop()


def final_details_screen(window, order):
    refresh(window)
    tkinter.Label(window, text="What is your name?").pack()
    i1 = tkinter.Entry(window, width=17)
    i1.pack()

    tkinter.Button(window, text="submit", command=lambda: order_result_screen(window, order, i1.get())).pack()

    window.mainloop()


def order_result_screen(window, order, customer_name):
    refresh(window)
    window.geometry("450x450")
    textbox = tkinter.Text(window)
    textbox.pack()

    printlogger = PrintLogger(textbox)
    sys.stdout = printlogger
    print(order.__str__)
    print(f"Customer Name: {customer_name}")
    tkinter.Button(window, text="Make another order", command=lambda: new_order(window)).pack()
    tkinter.Button(window, text="Finished", command=lambda: close(window)).pack()

    window.mainloop()

def new_order(window):
    window.geometry("300x200")
    order = Order([])
    screen1(window, order)

# stuff to log prints
class PrintLogger:
    def __init__(self, textbox):
        self.textbox = textbox

    def write(self, text):
        self.textbox.insert(tkinter.END, text)


def refresh(window):
    for widget in window.winfo_children():
        widget.destroy()


def close(window):
    window.destroy()
    window.quit()
