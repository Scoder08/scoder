from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog



root = Tk()
root.title("window1")
root.iconbitmap('icon/ss.ico')



vertical=Scale(root,from_=0,to=400)
vertical.pack(anchor=E)
horizontal=Scale(root,from_=0,to=400,orient=HORIZONTAL)
horizontal.pack()

def p():
	root.geometry(str(horizontal.get())+"x"+str(vertical.get()))

btn=Button(root,text="size",command=p).pack()


root.mainloop()