from desserts import *
import tkinter

def gui_main():
    order = Order([])
    window = tkinter.Tk()
    window.title("Dessert Shop")
    window.geometry("300x200")
    window.configure(background="white")
    screen1(window, order)



def screen1(window, order):
    refresh(window)
    l = tkinter.Label(window, text = "What would you like to add to the order?",)
    l.config(font = ("Courier", 9))
    l.pack()
    b1 = tkinter.Button(window, text = "Candy", command = lambda : candy_screen(window, order)).pack()
    b2 = tkinter.Button(window, text = "Cookie", ).pack()
    b3 = tkinter.Button(window, text = "Ice Cream", ).pack()
    b4 = tkinter.Button(window, text = "Sundae", ).pack()
    b5 = tkinter.Button(window, text = "Done with order").pack()
    T = tkinter.Text(window, height=2, width=20, )
    window.mainloop()

def candy_screen(window, order):
    refresh(window)
    l1 = tkinter.Label(window, text = "What type of candy would you like to order?").pack()
    i1 = tkinter.Text(window, height=1, width=35).pack()
    b1 = tkinter.Button(window, text="I want to go back :(", command= lambda : screen1(window, order)).pack()
    window.mainloop()

def refresh(window):
    for widget in window.winfo_children():
        widget.destroy()