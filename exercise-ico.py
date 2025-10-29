from tkinter import *

root=Tk()
# Set window size
root.geometry("400x200")
# Set window color
root['bg']='pink'

Label(root,text="Changed the window Icon").pack()
# Set window icon
root.iconbitmap('shy.ico')

root.mainloop()