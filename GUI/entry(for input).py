from tkinter import *

root = Tk()

e=Entry(root,width=30,borderwidth=3)
e.pack()
e.insert(0,"Enter your Name")

def myclick():
	Hello="Hello "+ e.get()
	myLable=Label(root, text=Hello.upper(),fg="blue")
	myLable.pack()



mybutton=Button(root,text="Submit", command=myclick, fg="white",bg="black")
mybutton.pack()

root.mainloop() 