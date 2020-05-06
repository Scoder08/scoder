from tkinter import *
from PIL import ImageTk,Image



root = Tk()
root.title("window1")
root.iconbitmap('icon/ss.ico')
options=["Monday",
	"Tuesday",
	"Wednesday",
	"Thrusday",
	"Friday",
	"Saturday"
	]

clicked=StringVar()
clicked.set(options[0])
def Show():
	lbl=Label(root,text=clicked.get()).pack()



drop=OptionMenu(root,clicked,*options).pack()

btn=Button(root,text="Show",command=Show).pack()




root.mainloop()