from tkinter import *
from PIL import ImageTk, Image

main = Tk()
main.title('Student Management System')
main.geometry('350x600')
main.resizable(0, 0)
main.iconbitmap('logo1.ico')

img = ImageTk.PhotoImage(Image.open("BSULOGO.png"))
imgLabel = Label(main, image = img)
imgLabel.place(
    x = 0, 
    y = 0
    )

label_frame = Frame(main, bg = 'white')
label_frame.place(
    x = 0, 
    y = 115, 
    height = 125, 
    width = 350
    )

Name = Label(
    label_frame, 
    text = " Student \n Management \n System", 
    font = ('Roboto', 25), 
    bg = '#FFFFFF', 
    fg = '#22263d'
    )
Name.place(
    relx = 0.5, 
    rely = 0.5, 
    anchor = CENTER
    )

image_frame = Frame(main, bg = 'red')
image_frame.place(x = 0, y = 240, height = 400, width = 350)

pic1 = Image.open("image2.png")
pic2 = pic1.resize((350, 500))
img2 = ImageTk.PhotoImage(pic2)
imgLabel2 = Label(image_frame, image = img2)
imgLabel2.place(x = 0, y = 0)

button = Button(
    image_frame, 
    text = "Click Here", 
    width = 25, 
    height = 2, 
    bg = "#22263d", 
    fg = "#FFFFFF", 
    font = ('Roboto', 12)
    ).place(x = 60, y = 280)

main.mainloop()