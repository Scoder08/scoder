from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox



root = Tk()
root.title("window1")
root.iconbitmap('icon/ss.ico')

global img
img=ImageTk.PhotoImage(Image.open("images/1.jpg"))

def opens():
	top=Toplevel()
	top.title("window2")
	lbl=Label(top,text="Hello world").pack()
	mylbl=Label(top,image=img).pack()
	btn2=Button(top,text="Exit",command=top.destroy).pack()


btn=Button(root,text="Open second window",command=opens).pack()


root.mainloop()