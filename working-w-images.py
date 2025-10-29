from tkinter import *
from PIL import ImageTk, Image
root=Tk()
# Set window size
root.geometry("400x200")
# Set window color
root['bg']='pink' 
Label(root,text="Working with image").pack()

# Load an image in the script
img=Image.open("wow.jpeg")

# Resize the Image using resize method
resized_image=img.resize((100,100))
new_image=ImageTk.PhotoImage(resized_image)
Label(root,image=new_image).pack()
root.mainloop()