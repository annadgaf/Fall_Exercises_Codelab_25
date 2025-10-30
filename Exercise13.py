from tkinter import *
import tkinter.messagebox

root = Tk()
root.title('Display Name')
root.geometry('400x200')
root.config(bg = '#FFB6C1')

def onClick():
    name = e1.get()
    s = f' Your name is : {name}'
    l2.configure(text = s)


l1 = Label(
    root, 
    text = "Enter Name", 
    bg = '#FFB6C1', 
    fg = "Black", 
    font = ("Lobster", 12)
    )
l1.place(
    x = 10, 
    y = 20
    )

e1 = Entry(
    root, 
    font = ("Lobster", 12)
    )
e1.place(
    x = 120, 
    y = 20
    )

b1 = Button(
    root, 
    text = "Show Name", 
    fg = "Black", 
    bg = "#001111", 
    font = ("Lobster", 12), 
    command = onClick
    )

b1.place(
    x = 140, 
    y = 60
    )

l2 = Label(
    root, 
    text = "Your Name is ", 
    bg = '#FFB6C1', 
    fg = "Black", 
    font = ("Lobster", 12)
    )
l2.place(
    x = 10, 
    y = 100
    )

root.mainloop()