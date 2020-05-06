from tkinter import *
from PIL import ImageTk,Image



root = Tk()
root.title("window1")
root.iconbitmap('icon/ss.ico')

var = StringVar()

def check():
	labl=Label(root,text=var.get()).pack()

c=Checkbutton(root,text="Check me",variable=var,onvalue="On",offvalue="OFF",command=check)
c.deselect()
c.pack()






root.mainloop()