# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
root=Tk()
# Define the geometry and title of the window
root.geometry("300x300")
root.title("Working with images")

# Create an object of tkinder ImageTk
img = ImageTk.PhotoImage(Image.open("shy.png"))

# Create a Label Widget to display the text or Image
label=Label(root, image=img)
label.pack()

root.mainloop()


img=Image.open("shy.png")
resized_image=img.resize((100,100))
new_image=ImageTk.PhotoImage(resized_image)
Label(root,image=new_image).pack()

