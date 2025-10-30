from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.geometry("400x200")
root['bg']='white'
Label(root,text="Changed the window Icon").pack()
root.iconphoto(False,ImageTk.PhotoImage(file="shy.png"))
root.mainloop()