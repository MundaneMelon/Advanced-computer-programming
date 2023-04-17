from desserts import *
import tkinter

def gui_main():
    window = tkinter.Tk()
    window.title("Dessert Shop")
    window.geometry("300x200")
    window.configure(background="white")
    screen1(window)


def screen1(window):
    l = tkinter.Label(window, text = "What would you like to add to the order?",)
    l.config(font = ("Courier", 9))
    l.pack()
    b1 = tkinter.Button(window, text = "Candy", command = lambda : candy_screen(window)).pack()
    b2 = tkinter.Button(window, text = "Cookie", ).pack()
    b3 = tkinter.Button(window, text = "Ice Cream", ).pack()
    b4 = tkinter.Button(window, text = "Sundae", ).pack()
    b5 = tkinter.Button(window, text = "Done with order").pack()
    T = tkinter.Text(window, height=2, width=20, )
    window.mainloop()

def candy_screen(window):
    refresh(window)
    window.mainloop()

def refresh(window):


