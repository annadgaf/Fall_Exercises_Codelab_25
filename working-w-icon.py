from tkinter import *
from PIL import ImageTk, Image
root=Tk()
# Set window size
root.geometry("400x200")
# Set window color
root['bg']='white'
Label(root,text="Changed the window Icon").pack()
# Set the window icon
root.iconphoto(False,ImageTk.PhotoImage(file="shy.png"))
root.mainloop()