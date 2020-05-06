from tkinter import *

root = Tk()

# creating a label widget
myLable1=Label(root, text="Hello World!!")
myLable2=Label(root, text="Its Shresth!!")

#shoving it onto the screen
myLable1.grid(row=0,column=0)
myLable2.grid(row=1,column=1)

root.mainloop()