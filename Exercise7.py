from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.geometry("300x300")
root.title("Working with images")

img = ImageTk.PhotoImage(Image.open("shy.png"))

label = Label(root, image = img)
label.pack()

root.mainloop()