from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox



root = Tk()
root.title("Frames")
root.iconbitmap('icon/ss.ico')

def popup():
	response=messagebox.showerror("Message","Hello World")
	Label(root,text=response).pack()
	



Button(root,text="Popup",command=popup).pack()


root.mainloop()