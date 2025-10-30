from tkinter import *
from PIL import ImageTk, Image

root=Tk()

root.geometry("400x200")
root['bg']='pink' 
Label(root,text="Working with image").pack()

img=Image.open("wow.jpeg")

resized_image=img.resize((100,100))
new_image=ImageTk.PhotoImage(resized_image)

Label(root,image=new_image).pack()
root.mainloop()