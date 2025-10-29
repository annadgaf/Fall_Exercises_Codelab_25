from tkinter import *

root = Tk()
root.title("First App")
root.geometry("400x200")
l = Label(root, text = "Hello!",
        fg = "purple",
        bg = "#FFFFFF",
        font = ('Roboto', 25))
l.pack()
l1 = Label(root, text = "My name is Anna",
           fg = "pink",
           bg = "#FFFFFF",
           font = ('Roboto', 10))
l1.pack()
l2 = Label(root, text = "I am studying in Bath Spa University Academic Center, RAK \
\n I am enrolled in BSc CS Year 2, Group 1",
fg = "#FFFFFF", bg = "#000000", font = ('Roboto', 8))
l2.pack()
root.mainloop()