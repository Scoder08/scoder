from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog



root = Tk()
root.title("window1")
root.iconbitmap('icon/ss.ico')



def opens():
	global img
	root.filename=filedialog.askopenfilename(initialdir="/Users/shres/Desktop/gui/images",title="Select a file",filetypes=(("ico files","*.ico"),("all files","*.*")))
	img=ImageTk.PhotoImage(Image.open(root.filename))
	imm=Label(image=img).pack()


btn=Button(root,text="Choose File",command=opens).pack()

root.mainloop()