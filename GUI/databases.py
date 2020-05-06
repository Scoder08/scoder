from tkinter import *
from PIL import ImageTk,Image
import sqlite3


root = Tk()
root.title("window1")
root.iconbitmap('icon/ss.ico')


#create table
'''c.execute("""CREATE TABLE addresses (
	first_name text,
	last_name text,
	address text,
	city text,
	state text,
	zipcode integer
	)""")
'''

# submit function
def submit():
#create database or connect to one
	conn=sqlite3.connect("address_book.db")

#Create cursor
	c=conn.cursor()

	c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address,:city,:state,:zipcode)",
	{
	'f_name': f_name.get(),
	'l_name': l_name.get(),
	'address': address.get(),
	'city': city.get(),
	'state': state.get(),
	'zipcode': zipcode.get()
	})


	conn.commit()

	conn.close()
	#clear text boxes
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

#query func
def query():
	#create database or connect to one
	conn=sqlite3.connect("address_book.db")

#Create cursor
	c=conn.cursor()
	c.execute("SELECT *,oid FROM addresses")
	records=c.fetchall()
	#print(records)

	print_records=''
	for record in records:
		print_records+=str(record[6])+". "+str(record[0])+" "+str(record[1])+"\n"
	querylabel=Label(root,text=print_records).grid(row=8,column=0,columnspan=2)




	conn.commit()

	conn.close()

#delete function
def op():
	global delete_box
	dltlbl=Label(root,text="ID: ").grid(row=10,column=0,padx=10)
	delete_box=Entry(root,width=28)
	delb=Button(root,text="Delete",command=lambda: Del(delete_box.get()))
	upb=Button(root,text="Update",command=lambda: update(delete_box.get()))
	delete_box.grid(row=10,column=1,padx=10,pady=5,columnspan=2,sticky="W")
	delb.grid(row=11,column=1,padx=25,sticky="W")
	upb.grid(row=11,column=1,padx=25,sticky="E")
def Del(v):
	global delete_box
	delete_box.delete(0,END)
	conn=sqlite3.connect("address_book.db")

#Create cursor
	c=conn.cursor()
	c.execute("DELETE FROM addresses WHERE oid="+ v)



	
	conn.commit()

	conn.close()



def save(v):
	conn=sqlite3.connect("address_book.db")

#Create cursor
	c=conn.cursor()
	c.execute("""UPDATE addresses SET
		first_name=:first,
		last_name=:last,
		address=:address,
		city=:city,
		state=:state,
		zipcode=:zipcode

		WHERE oid=:oid""",
		{
		'first':f_namee.get(),
		'last':l_namee.get(),
		'address':addresse.get(),
		'city':citye.get(),
		'state':statee.get(),
		'zipcode':zipcodee.get(),
		'oid':v
		})
	editor.destroy()
	saved=Label(root,text="Saved",fg="green",font=12).grid(row=12,column=0,columnspan=2)





	conn.commit()

	conn.close()









def update(v):
	global editor
	editor = Tk()
	editor.title("Update")
	editor.iconbitmap('icon/ss.ico')
	editor.geometry("400x200")
	global f_namee
	global l_namee
	global addresse
	global citye
	global statee
	global zipcodee

	f_namee=Entry(editor,width=30)
	f_namee.grid(row=1,column=0,padx=10)
	l_namee=Entry(editor,width=30)
	l_namee.grid(row=1,column=1,padx=10)
	addresse=Entry(editor,width=30)
	addresse.grid(row=3,column=0,padx=10)
	citye=Entry(editor,width=30)
	citye.grid(row=3,column=1,padx=10)
	statee=Entry(editor,width=30)
	statee.grid(row=5,column=0,padx=10)
	zipcodee=Entry(editor,width=30)
	zipcodee.grid(row=5,column=1,padx=10)





	#box labels
	f_namee_label = Label(editor,text="First Name").grid(row=0,column=0 )
	l_namee_label = Label(editor,text="Last Name").grid(row=0,column=1)
	addresse_label = Label(editor,text="Address").grid(row=2,column=0)
	citye_label = Label(editor,text="City").grid(row=2,column=1)
	statee_label = Label(editor,text="State").grid(row=4,column=0)
	zipcodee_label = Label(editor,text="Zipcode").grid(row=4,column=1)

	sve=Button(editor,text="Save Record",command=lambda :save(v)).grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=150)

	conn=sqlite3.connect("address_book.db")

#Create cursor
	c=conn.cursor()
	c.execute("SELECT * FROM addresses WHERE oid="+v)


	records=c.fetchall()
	#print(records)

	for record in records:
		f_namee.insert(0,record[0])
		l_namee.insert(0,record[1])
		addresse.insert(0,record[2])
		citye.insert(0,record[3])
		statee.insert(0,record[4])
		zipcodee.insert(0,record[5])


	conn.commit()

	conn.close()


	
#Create Text Boxes
f_name=Entry(root,width=30)
f_name.grid(row=1,column=0,padx=10)
l_name=Entry(root,width=30)
l_name.grid(row=1,column=1,padx=10)
address=Entry(root,width=30)
address.grid(row=3,column=0,padx=10)
city=Entry(root,width=30)
city.grid(row=3,column=1,padx=10)
state=Entry(root,width=30)
state.grid(row=5,column=0,padx=10)
zipcode=Entry(root,width=30)
zipcode.grid(row=5,column=1,padx=10)




#box labels
f_name_label = Label(root,text="First Name").grid(row=0,column=0 )
l_name_label = Label(root,text="Last Name").grid(row=0,column=1)
address_label = Label(root,text="Address").grid(row=2,column=0)
city_label = Label(root,text="City").grid(row=2,column=1)
state_label = Label(root,text="State").grid(row=4,column=0)
zipcode_label = Label(root,text="Zipcode").grid(row=4,column=1)

#submit Button
submit=Button(root,text="Add Record To Database",command=submit).grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=109)
#query button
query=Button(root,text="Show Records",command=query).grid(row=7,column=0,columnspan=2,pady=10,padx=10,ipadx=137)
#delete button
dlt=Button(root,text="Change Records",command=op).grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=136)


#commit changes

root.mainloop()