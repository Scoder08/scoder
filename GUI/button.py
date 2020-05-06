from tkinter import *

root = Tk()
def myclick():
	myLable=Label(root, text="Look! you clicked it.",fg="blue")
	myLable.pack()



mybutton=Button(root,text="Click me!!", command=myclick, fg="white",bg="black")
mybutton.pack()

root.mainloop()