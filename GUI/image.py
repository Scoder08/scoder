from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Images")
root.iconbitmap('icon/ss.ico')







img1=ImageTk.PhotoImage(Image.open("images/1.jpg"))
img2=ImageTk.PhotoImage(Image.open("images/2.jpg"))
img3=ImageTk.PhotoImage(Image.open("images/3.jpg"))
img4=ImageTk.PhotoImage(Image.open("images/4.jpg"))
img5=ImageTk.PhotoImage(Image.open("images/5.jpg"))


image_list=[img1,img2,img3,img4,img5]



label=Label(image=img1)
label.grid(row=0,column=0,columnspan=3)



def Next(image_number):
	global label
	global button_forward
	global button_back
	global image_list

	label.grid_forget()
	label=Label(image=image_list[image_number-1])
	#Status--------------------------------------------------------
	status=Label(root,text="Image "+str(image_number)+ " of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)

	button_next=Button(root,text=">>",command=lambda: Next(image_number+1))
	button_previous=Button(root,text="<<",command=lambda: Next(image_number-1))
	label.grid(row=0,column=0,columnspan=3)
	button_previous.grid(row=1,column=0)
	button_next.grid(row=1,column=2)
	status.grid(row=3,column=0,columnspan=3,sticky=W+E)
	if image_number==len(image_list):
		button_next=Button(root,text=">>",state=DISABLED)
		button_next.grid(row=1,column=2)

	if image_number==1:
		button_previous=Button(root,text="<<",command=Previous,state=DISABLED)
		button_previous.grid(row=1,column=0)




def Previous(image_number):
	global label
	global button_forward
	global button_back

	label.grid_forget()

	label=Label(image=image_list[image_number-1])
	button_next=Button(root,text=">>",command=lambda: Next(image_number+1))
	button_previous=Button(root,text="<<",command=lambda: Next(image_number-1))
	label.grid(row=0,column=0,columnspan=3)
	button_previous.grid(row=1,column=0)
	button_next.grid(row=1,column=2)

status=Label(root,text="Image 1 of " + str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
status.grid(row=3,column=0,columnspan=3,sticky=W+E)

button_previous=Button(root,text="<<",command=Previous,state=DISABLED)
button_previous.grid(row=1,column=0)

button_next=Button(root,text=">>",command=lambda: Next(2))
button_next.grid(row=1,column=2)

button_quit=Button(root,text="Exit",command=root.quit)
button_quit.grid(row=1,column=1,pady=5)

root.mainloop()