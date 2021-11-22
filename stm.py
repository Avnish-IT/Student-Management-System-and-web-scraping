from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import matplotlib.pyplot as plt
import requests
import numpy as np
import bs4


def add_di1():
	main_window.withdraw()
	add_window.deiconify()

def add_di2():
	add_window.withdraw()
	main_window.deiconify()

def view():
	main_window.withdraw()
	view_window.deiconify()
	view_window.deiconify()
	view_window_st_data.delete(1.0,END)
	info=""
	con=None
	try:
		con=connect("avs.db")
		cursor=con.cursor()
		sql="select * from student"
		cursor.execute(sql)
		data=cursor.fetchall()
		for d in data:
		    info=info + " rno: " + str(d[0]) + " name: " + str(d[1]) +" marks: " + str(d[2]) + "\n"
		view_window_st_data.insert(INSERT, info)
	except Exception as e:
		showerror("Issue", e)
	finally:
		if con is not None:
			con.close()

def view_di():
	view_window.withdraw()
	main_window.deiconify()

def add():
	if (add_window_ent_rno.get() == ""):
		showerror('Issue',"rno is not entered")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (add_window_ent_rno.get().isalpha() == True):
		showerror('Issue',"Invalid rno")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (int(add_window_ent_rno.get()) <= 0) :
		showerror('Issue',"Rno entered is negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (add_window_ent_name.get() == ""):
		showerror('Issue',"Name is not entered")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (len(add_window_ent_name.get()) < 2):
		showerror('issue',"Too short name")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (((add_window_ent_name.get()).isalpha()) == False):
		showerror('Issue',"Enter alphabets only")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (add_window_ent_marks.get() == ""):
		showerror('Issue',"Marks are not entered")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif (add_window_ent_marks.get().isdigit() == False):
		showerror('Issue',"Enter a proper number in marks")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif int(add_window_ent_marks.get()) < 0:
		showerror('Issue',"Marks u entered are negative")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	elif int(add_window_ent_marks.get()) > 100:
		showerror('Issue',"Marks out of bound")
		add_window_ent_rno.delete(0, END)
		add_window_ent_name.delete(0, END)
		add_window_ent_marks.delete(0, END)
		add_window_ent_rno.focus()

	else:
		con = None
		try:
			rno = int(add_window_ent_rno.get())
			name = add_window_ent_name.get()
			marks = int(add_window_ent_marks.get())
			con = connect("avs.db")
			cursor = con.cursor()
			sql = "insert into student values('%d', '%s', '%d')"
			cursor.execute(sql % (rno, name, marks))
			con.commit()
			showinfo("Success", "Record added")
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_marks.delete(0, END)
			add_window_ent_rno.focus()		
		except Exception as e:
			showerror("Issue", e)
			add_window_ent_rno.delete(0, END)
			add_window_ent_name.delete(0, END)
			add_window_ent_marks.delete(0, END)
			add_window_ent_rno.focus()	
		finally:
			if con is not None:
				con.close()

def update_di1():
	main_window.withdraw()
	update_window.deiconify()

def update_di2():
	update_window.withdraw()
	main_window.deiconify()

def update():
	if (update_window_ent_rno.get() == ""):
		showerror('Issue',"rno is not entered")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (update_window_ent_rno.get().isalpha() == True):
		showerror('Issue',"Invalid rno")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (int(update_window_ent_rno.get()) <= 0) :
		showerror('Issue',"Rno entered is negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (update_window_ent_name.get() == ""):
		showerror('Issue',"Name is not entered")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (len(update_window_ent_name.get()) < 2):
		showerror('issue',"Too short name")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (((update_window_ent_name.get()).isalpha()) == False):
		showerror('Issue',"Enter alphabets only")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (update_window_ent_marks.get() == ""):
		showerror('Issue',"Marks are not entered")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif (update_window_ent_marks.get().isdigit() == False):
		showerror('Issue',"Enter a number in marks")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif int(update_window_ent_marks.get()) < 0:
		showerror('Issue',"Marks u entered are negative")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	elif int(update_window_ent_marks.get()) > 100:
		showerror('Issue',"Marks out of bound")
		update_window_ent_rno.delete(0, END)
		update_window_ent_name.delete(0, END)
		update_window_ent_marks.delete(0, END)
		update_window_ent_rno.focus()

	else:
		con = None
		try:
			rno = int(update_window_ent_rno.get())
			name = update_window_ent_name.get()
			marks = int(update_window_ent_marks.get())
			con = connect("avs.db")
			cursor = con.cursor()
			sql = "update student set name = '%s', marks = '%d' where rno = '%d'"
			cursor.execute(sql % (name, marks, rno))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("Success", "record updated")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)
				update_window_ent_rno.focus()
			else:
				showwarning('Issue',"Record is not existing")
				update_window_ent_rno.delete(0, END)
				update_window_ent_name.delete(0, END)
				update_window_ent_marks.delete(0, END)
				update_window_ent_rno.focus()
		except Exception as e:
			showerror("Issue", e)
		finally:
			if con is not None:
					con.close()
	    

def delete_di1():
	main_window.withdraw()
	delete_window.deiconify()

def delete_di2():
	delete_window.withdraw()
	main_window.deiconify()

def delete():
	con = None
	if (delete_window_ent_rno.get() == ""):
		showerror('issue',"Please enter number")
		delete_window_ent_rno.delete(0, END)
		delete_window_ent_rno.focus()
	elif ((delete_window_ent_rno.get()).isalpha() == True):
		showerror('Issue',"Rno should be integer")
		delete_window_ent_rno.delete(0, END)
		delete_window_ent_rno.focus()
	elif (int(delete_window_ent_rno.get()) <= 0):
		showerror('Issue',"Rno is invalid")
		delete_window_ent_rno.delete(0, END)
		delete_window_ent_rno.focus()
	else:
		try:
			con = connect("avs.db")
			cursor = con.cursor()
			rno = int(delete_window_ent_rno.get())
			sql = "delete from student where rno = '%d' "
			cursor.execute(sql % (rno))
			if cursor.rowcount > 0:
				con.commit()
				showinfo("Success", "Record deleted ")
				delete_window_ent_rno.delete(0, END)
				delete_window_ent_rno.focus()
			else:
				showerror("issue", "Student donot exist")
				delete_window_ent_rno.delete(0, END)
				delete_window_ent_rno.focus()
		except Exception as e:
			showerror("Issue", e)
			delete_window_ent_rno.delete(0, END)
			delete_window_ent_rno.focus()
		finally:
			if con is not None:
				con.close()



def bar_graph():
	try:
		con=connect("avs.db")
		sql="select name, marks from student"
		cursor=con.cursor()	
		cursor.execute(sql)
		name=[]
		marks=[]
		for row in cursor.fetchall():
			name.append(row[0])
			marks.append(row[1])
		name_len=np.arange(len(name))
		plt.bar(name, marks)
		plt.xlabel("Students")
		plt.ylabel("Marks")
		plt.xticks(name_len, name)
		plt.show()
	except Exception as e:
		showerror("Issue", e)	
		




def temperature():
	city_name='Mumbai'
	a1="https://api.openweathermap.org/data/2.5/weather?units=metric"
	a2="&q=" + city_name
	a3="&appid=" + "c6e315d09197cec231495138183954bd"
	wa=a1+a2+a3

	response=requests.get(wa)

	data=response.json()


	temp=data['main']['temp']
	return temp

def qotd():
	wa="https://www.brainyquote.com/quote_of_the_day"
	res=requests.get(wa)
	data=bs4.BeautifulSoup(res.text, "html.parser")
	info=data.find('img',{'class':'p-qotd'})
	msg=info['alt']
	return msg

def location():
	try:
		wa="https://ipinfo.io/"
		response=requests.get(wa)
		data=response.json()
		city_name=data['city']
		return city_name

	except Exception as e:
		print("issue", e)

    




main_window=Tk()
main_window.title("S.M.S")
main_window.geometry("1000x500+400+100")

f=("Calibri", 18, 'bold')
main_window_btn_add=Button(main_window, text="Add", width=10, font=f, command=add_di1)
main_window_btn_view=Button(main_window, text="View", width=10, font=f, command=view)
main_window_btn_update=Button(main_window, text="Update", width=10, font=f, command=update_di1)
main_window_btn_delete=Button(main_window, text="Delete", width=10, font=f, command=delete_di1)
main_window_btn_charts=Button(main_window, text="Charts", width=10, font=f, command=bar_graph)
main_window_lbl_loc=Label(main_window, text="Location: ", font=f)
main_window_lbl_loc.config(text=f"Loc: {str(location())}")
main_window_lbl_loc.place(x=230, y=350)
main_window_lbl_temp=Label(main_window, text="Temp:" , font=f)
main_window_lbl_temp.config(text=f"Temp: {str(temperature())}")
main_window_lbl_temp.place(x=580, y=350)
main_window_lbl_temp=Label(main_window, text="QOTD: " , font=f)
main_window_lbl_temp.config(text=f"QOTD: {str(qotd())}")
main_window_lbl_temp.place(x=20, y=400)






main_window_btn_add.pack(pady=8)
main_window_btn_view.pack(pady=8)
main_window_btn_update.pack(pady=8)
main_window_btn_delete.pack(pady=8)
main_window_btn_charts.pack(pady=8)




add_window=Toplevel(main_window)
add_window.title("Add Stu.")
add_window.geometry("1000x500+400+100")

add_window_lbl_rno=Label(add_window, text="Enter rno", font=f)
add_window_ent_rno=Entry(add_window, bd=5, font=f)
add_window_lbl_name=Label(add_window, text="Enter Name", font=f)
add_window_ent_name=Entry(add_window, bd=5, font=f)
add_window_lbl_marks=Label(add_window, text="Enter Marks", font=f)
add_window_ent_marks=Entry(add_window, bd=5, font=f)
add_window_btn_save=Button(add_window, text="Save", font=f, command=add)
add_window_btn_back=Button(add_window, text="Back", font=f, command=add_di2)

add_window_lbl_rno.pack(pady=10)
add_window_ent_rno.pack(pady=10)
add_window_lbl_name.pack(pady=10)
add_window_ent_name.pack(pady=10)
add_window_lbl_marks.pack(pady=10)
add_window_ent_marks.pack(pady=10)
add_window_btn_save.pack(pady=10)
add_window_btn_back.pack(pady=10)

add_window.withdraw()



view_window=Toplevel(main_window)
view_window.title("View Stu.")
view_window.geometry("1000x500+400+100")
view_window_st_data=ScrolledText(view_window, width=50, height=20)
view_window_btn_back=Button(view_window,text="Back",font=f,command=view_di)

view_window_st_data.pack(pady=10)
view_window_btn_back.pack(pady=10)

view_window.withdraw()




update_window=Toplevel(main_window)
update_window.title("Update Stu.")
update_window.geometry("1000x500+400+100")

update_window_lbl_rno=Label(update_window, text="Enter rno", font=f)
update_window_ent_rno=Entry(update_window, bd=5, font=f)
update_window_lbl_name=Label(update_window, text="Enter Name", font=f)
update_window_ent_name=Entry(update_window, bd=5, font=f)
update_window_lbl_marks=Label(update_window, text="Enter Marks", font=f)
update_window_ent_marks=Entry(update_window, bd=5, font=f)
update_window_btn_save=Button(update_window, text="Save", font=f, command=update)
update_window_btn_back=Button(update_window, text="Back", font=f, command=update_di2)


update_window_lbl_rno.pack(pady=10)
update_window_ent_rno.pack(pady=10)
update_window_lbl_name.pack(pady=10)
update_window_ent_name.pack(pady=10)
update_window_lbl_marks.pack(pady=10)
update_window_ent_marks.pack(pady=10)
update_window_btn_save.pack(pady=10)
update_window_btn_back.pack(pady=10)

update_window.withdraw()



delete_window=Toplevel(main_window)
delete_window.title("Delete Stu.")
delete_window.geometry("1000x500+400+100")

delete_window_lbl_rno=Label(delete_window, text="Enter rno", font=f)
delete_window_ent_rno=Entry(delete_window, bd=5, font=f)
delete_window_btn_save=Button(delete_window, text="Save", font=f, command=delete)
delete_window_btn_back=Button(delete_window, text="Back", font=f, command=delete_di2)

delete_window_lbl_rno.pack(pady=10)
delete_window_ent_rno.pack(pady=10)
delete_window_btn_save.pack(pady=10)
delete_window_btn_back.pack(pady=10)

delete_window.withdraw()



main_window.mainloop()