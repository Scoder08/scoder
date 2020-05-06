from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Frames")
root.iconbitmap('icon/ss.ico')


topings=[
	("Cheese","Cheese"),
	("Onion","Onion"),	
	("Paneer","Paneer"),
	("Maghareeta","Maghareeta")
]

pizza=StringVar()
pizza.set(0)
for text,topping in topings:
	Radiobutton(root,text=text,variable=pizza,value=topping).pack(anchor=W)

def clicked(value):
	label= Label(root,text=value)
	label.pack()



#Radiobutton(root,text="Option 1",variable=r,value=1,command=lambda: clicked(r.get())).pack()
#Radiobutton(root,text="Option 2",variable=r,value=2,command=lambda: clicked(r.get())).pack()


#myButton=Button(root,text="click me",command=lambda: clicked(pizza.get())).pack()
root.mainloop()