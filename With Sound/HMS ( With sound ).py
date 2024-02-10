from tkinter import *

from tkinter import ttk

from tkinter import messagebox

import cx_Oracle

import pyttsx3

def main0():

	def main():
 
		try:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur = conn.cursor()

			x = cur.execute('select * from DOCTOR_RECORD')

		except:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur0 = conn.cursor()

			y = cur0.execute(

				"create table DOCTOR_RECORD (docid int , name varchar(20) , age varchar(10) , gender varchar(10) , city varchar(20) , specialist varchar(20) , address varchar(100) , mobilenumber varchar(20))")

			cur0.execute(

				"insert into DOCTOR_RECORD values (0 ,'Vaibhav' ,'16', 'Male' , 'Aligarh' ,'Phyisicist' , 'Rambagh' ,'0000000001')")

			cur0.execute("commit")

		try:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur = conn.cursor()

			x = cur.execute('select * from PATIENT_RECORD')
		except:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur0 = conn.cursor()

			y = cur0.execute(

				"create table PATIENT_RECORD (patid int , name varchar(20) ,disease  varchar(20),bgroup  varchar(20),dname  varchar(20), age varchar(10) , gender varchar(10) , city varchar(20) ,weight  varchar(20), height  varchar(20) , address varchar(100) , mobilenumber varchar(20))")

			cur0.execute("commit")

		try:   

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur = conn.cursor()

			x = cur.execute('select * from UNLOCK_FOR_ADMIN')

		except:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur0 = conn.cursor()

			cur0.execute("create table UNLOCK_FOR_ADMIN(username varchar(20),pass varchar(20))")

			cur0.execute("insert into UNLOCK_FOR_ADMIN values('mukesh',1000)")

			cur0.execute("insert into UNLOCK_FOR_ADMIN values('rohit',1001)")

			cur0.execute("commit")

		try:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur = conn.cursor()

			x = cur.execute('select * from UNLOCK_FOR_USER')

		except:

			conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

			cur0 = conn.cursor()

			cur0.execute("create table UNLOCK_FOR_USER(username varchar(20),pass varchar(20))")

			cur0.execute("insert into UNLOCK_FOR_USER values('vaibhav',100)")

			cur0.execute("commit")

		def fa():

			def doctt():

				r = Tk()

				r.iconbitmap(r"hms.ico")

				r.title('Hospital Managment System')

				r.geometry('1365x727')

				r.config(bg="#6e6e48")

				DoctorID = IntVar()

				Name = StringVar()

				Specialist = StringVar()

				City = StringVar()

				Age = StringVar()

				Gender = StringVar()

				Address = StringVar()

				Mobile = StringVar()

				m = Frame(r)

				m.pack()
				c = Canvas(m, width=1365, height=704)

				c.pack()

				p = PhotoImage(file=r"hms14.png")

				c.create_image(0, 0, image=p, anchor="nw")

				lbltit = Label(m,font = ('castellar', 35, 'bold'), text="Hospital  Mangement  System", fg="#FF979E",bg="#622227", bd=7, anchor="w",relief="raise")

				lbltit.place(x=250,y=10)

				ButtonFrame = Frame(m, bd=2, width=1350, height=70, padx=18, pady=10, bg="#FF979E",relief='raise')

				ButtonFrame.place(x=10 ,y  = 590)

				DataFrameLEFT = LabelFrame(m, width=1000, height=600, bd=7, padx=20,fg='#FF979E', bg="#622227", relief='raise',text="Doctor information\n", font=('arial', 20, 'bold'))

				DataFrameLEFT.place(x=10 , y=150)

				DataFrameRIGHT = LabelFrame(m, bd=7, width=450, height=300, padx=31,fg='#FF979E', pady=3, bg="#622227",relief='raise', text="Doctor Details\n", font=('arial', 20, 'bold'))

				DataFrameRIGHT.place(x=890,y=150)

				lblDoctorID = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Doctor ID",fg='#FF979E', bg="#622227",relief ='ridge',bd=7, padx=2,pady=2,width=13)

				lblDoctorID.grid(row=0, column=0, sticky=W)

				txtDoctorID = Entry(DataFrameLEFT,bg='#FF979E', font=('arial', 12, 'bold'), textvariable=DoctorID,fg='#622227',relief ='ridge',bd=12, width=40,justify='center')

				txtDoctorID.grid(row=0, column=1)

				txtDoctorID.focus()

				lblname = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Name",fg='#FF979E', bg="#622227", padx=2,relief ='ridge',bd=7, pady=3,width=13)

				lblname.grid(row=1, column=0, sticky=W)

				txtname = Entry(DataFrameLEFT,bg='#FF979E', font=('arial', 12, 'bold'),fg='#622227', textvariable=Name, width=40,relief ='ridge',bd=12,justify='center')

				txtname.grid(row=1, column=1)

				txtname.focus()

				lblage = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Age (yrs)",fg='#FF979E', bg="#622227", padx=2, pady=3,relief ='ridge',bd=7,width=13)

				lblage.grid(row=2, column=0, sticky=W)

				txtage = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),bg='#FF979E',fg='#622227', textvariable=Age, width=40,justify='center',relief ='ridge',bd=12)

				txtage.grid(row=2, column=1)

				txtage.focus()

				lblgen = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Gender",fg='#FF979E', bg="#622227", padx=2, pady=3,relief ='ridge',bd=7,width=13)

				lblgen.grid(row=3, column=0, sticky=W)

				txtgen = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),bg='#FF979E',fg='#622227', textvariable=Gender,justify='center', width=40,relief ='ridge',bd=12)

				txtgen.grid(row=3, column=1)

				txtgen.focus()

				lblcity = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="City",relief ='ridge',bd=7,fg='#FF979E', bg="#622227", padx=2, pady=2,width=13)

				lblcity.grid(row=4, column=0, sticky=W)

				txtcity = Entry(DataFrameLEFT, textvariable=City,bg='#FF979E',fg='#622227', font=('arial', 12, 'bold'),justify='center', width=40,relief ='ridge',bd=12)

				txtcity.grid(row=4, column=1)

				txtcity.focus()

				lblspc = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Specialist in",fg='#FF979E', bg="#622227", padx=2,pady=2,relief ='ridge',bd=7,width=13)

				lblspc.grid(row=5, column=0, sticky=W)

				txtspc = Entry(DataFrameLEFT, textvariable=Specialist,fg='#622227',bg='#FF979E', font=('arial', 12, 'bold'),justify='center', width=40,relief ='ridge',bd=12)

				txtspc.grid(row=5, column=1)

				txtspc.focus()

				lbladd = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Address",fg='#FF979E', bg="#622227", padx=2, pady=3,relief ='ridge',bd=7,width=13)


				lbladd.grid(row=6, column=0, sticky=W)

				txtadd = Entry(DataFrameLEFT,bg='#FF979E',fg='#622227', font=('arial', 12, 'bold'), textvariable=Address, width=40,justify='center',relief ='ridge',bd=12)

				txtadd.grid(row=6, column=1)

				txtadd.focus()

				lblmob = Label(DataFrameLEFT, font=('castellar', 11, 'bold'), text="Mobile-Number",fg='#FF979E', bg="#622227", padx=2,pady=3,relief ='ridge',bd=7,width=13)

				lblmob.grid(row=7, column=0, sticky=W)

				txtmob = Entry(DataFrameLEFT, font=('arial', 12, 'bold'),fg='#622227', textvariable=Mobile,bg='#FF979E', width=40,justify='center',relief ='ridge',bd=12)

				txtmob.grid(row=7, column=1)

				txtmob.focus()

				def iexit():

					iexit = messagebox.askokcancel("Hospital Managment System", " Do you want to exit ")

					if iexit > 0:

						r.destroy()

						fa()

						return

				def cleardata():

					txtDoctorID.delete(0, END)

					txtname.delete(0, END)

					txtage.delete(0, END)

					txtgen.delete(0, END)

					txtcity.delete(0, END)

					txtspc.delete(0, END)

					txtadd.delete(0, END)

					txtmob.delete(0, END)

				def viewdata():

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					cur.execute("select * from DOCTOR_RECORD")

					row = cur.fetchall()
					conn.close

					return row

				def ssearchdata(x):

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					cur.execute("select * from DOCTOR_RECORD where docid = %d  " % x)

					row = cur.fetchall()

					conn.close

					return row

				def addrecorddoc(txtDoctor, txtname, txtspc, txtcity, txtage, txtgen, txtadd, txtmob):

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					cur.execute("insert into DOCTOR_RECORD values (%d , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (

					txtDoctor, txtname, txtspc, txtcity, txtage, txtgen, txtadd, txtmob))

					cur.execute("commit")

					conn.close

				def deleterec(docid):

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					cur.execute("delete  from DOCTOR_RECORD where docid = %d" % docid)

					cur.execute("commit")

					conn.close

				def adddata():

					addrecorddoc(int(txtDoctorID.get()), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtspc.get(), txtadd.get(), txtmob.get())

					doclist.delete(0, END)

					doclist.insert(END, (

					txtDoctorID.get(), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtspc.get(), txtadd.get(),txtmob.get()))

					messagebox.showinfo('Hospital Mangement System','New Doctor Added Successfully')

				def displaydata():

					doclist.delete(0, END)

					for row in viewdata():

						doclist.insert(END, row, str(" "))

				def recorddoc(event):

					global sd

					searchpat = doclist.curselection()[0]

					sd = doclist.get(searchpat)

					txtDoctorID.delete(0, END)

					txtDoctorID.insert(END, sd[0])

					txtname.delete(0, END)

					txtname.insert(END, sd[1])

					txtage.delete(0, END)

					txtage.insert(END, sd[2])

					txtgen.delete(0, END)

					txtgen.insert(END, sd[3])

					txtcity.delete(0, END)

					txtcity.insert(END, sd[4])

					txtspc.delete(0, END)

					txtspc.insert(END, sd[5])

					txtadd.delete(0, END)

					txtadd.insert(END, sd[6])

					txtmob.delete(0, END)

					txtmob.insert(END, sd[7])

				def deletedata():

					searchpat = doclist.curselection()[0]

					sd = doclist.get(searchpat)

					deleterec(sd[0])

					cleardata()

					displaydata()

					messagebox.showinfo('Hospital Mangement System', ' Doctor Deleted Successfully')

				def searchdata():

					doclist.delete(0, END)

					for row in ssearchdata(int(txtDoctorID.get())):

						cleardata()

						doclist.insert(END, row, str(""))

						x=row[1]

						x0=row[2]

						x1=row[5]

						x3=row[4]

						x4=row[3]

						x5=row[6]

						x6=row[7]

						x00=row[0]

						txtDoctorID.insert(0,x00)

						txtmob.insert(0,x6)

						txtadd.insert(0,x5)

						txtgen.insert(0,x4)

						txtcity.insert(0,x3)

						txtspc.insert(0,x1)

						txtage.insert(0,x0)

						txtname.insert(0,x)

				def update():

					searchpat = doclist.curselection()[0]

					sd = doclist.get(searchpat)

					doclist.delete(0, END)

					deleterec(sd[0])

					addrecorddoc(int(txtDoctorID.get()), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtspc.get(), txtadd.get(), txtmob.get())

					doclist.delete(0, END)

					doclist.insert(END, (int(txtDoctorID.get()), txtname.get(), txtage.get(), txtgen.get(), txtcity.get(),txtspc.get(), txtadd.get(), txtmob.get()))

					messagebox.showinfo('Hospital Mangement System', 'New Information Updated Successfully')

				scroll = Scrollbar(DataFrameRIGHT)

				scroll.grid(row=0, column=1, sticky='NS'),

				doclist = Listbox(DataFrameRIGHT, width=41, height=16, font=("arial", 12, "bold"),fg = '#622227',bg='#FF979E',yscrollcommand=scroll.set)

				doclist.bind('<<ListboxSelect>>',recorddoc)

				doclist.grid(row=0, column=0, padx=8)

				scroll.config(command=doclist.yview)

				def aadddata():

																								engine = pyttsx3.init()

																								rate = engine.getProperty('rate')

																								voices_in_our_pc=engine.getProperty('voices')

																								engine.setProperty('rate',150)

																								engine.setProperty('voice',voices_in_our_pc[1].id)

																								engine.say("New doctor added successfully")

																								engine.runAndWait()

																								adddata()
																								

				btn1 = Button(ButtonFrame, text="Add New", font=("arial", 20, "bold"), height=1, width=10, bd=7,fg='#FF979E',bg='#622227',command=aadddata,relief = 'raise')

				btn1.grid(row=0, column=0)

				def ddisplaydata():

																								engine = pyttsx3.init()

																								rate = engine.getProperty('rate')

																								voices_in_our_pc=engine.getProperty('voices')

																								engine.setProperty('rate',150)

																								engine.setProperty('voice',voices_in_our_pc[1].id)

																								engine.say("Displaying all the existing doctors")

																								engine.runAndWait()

																								displaydata()

				btn2 = Button(ButtonFrame, text="Display", font=("arial", 20, "bold"), height=1, width=10, bd=7,fg='#FF979E',bg='#622227',command=ddisplaydata,relief = 'raise')

				btn2.grid(row=0, column=1)

				def ccleardata():

																								engine = pyttsx3.init()

																								rate = engine.getProperty('rate')

																								voices_in_our_pc=engine.getProperty('voices')

																								engine.setProperty('rate',150)

																								engine.setProperty('voice',voices_in_our_pc[1].id)

																								engine.say("This will clear all the entry fields")

																								engine.runAndWait()

																								cleardata()

				btn3 = Button(ButtonFrame, text="Clear", font=("arial", 20, "bold"), height=1, width=10, bd=7,fg='#FF979E',bg='#622227',command=ccleardata,relief = 'raise')

				btn3.grid(row=0, column=2)

				def ddeletedata():

																								engine = pyttsx3.init()

																								rate = engine.getProperty('rate')

																								voices_in_our_pc=engine.getProperty('voices')

																								engine.setProperty('rate',150)

																								engine.setProperty('voice',voices_in_our_pc[1].id)

																								engine.say("Doctor deleted successfully")

																								engine.runAndWait()

																								deletedata()

				btn4 = Button(ButtonFrame, text="Delete", font=("arial", 20, "bold"), height=1, width=10, bd=7,fg='#FF979E',bg='#622227',command=ddeletedata,relief = 'raise')

				btn4.grid(row=0, column=3)

				btn5 = Button(ButtonFrame, text="Search", font=("arial", 20, "bold"), height=1, width=10, bd=7,fg='#FF979E',bg='#622227',command=searchdata,relief = 'raise')

				btn5.grid(row=0, column=4)

				def uupdate():

																								engine = pyttsx3.init()

																								rate = engine.getProperty('rate')

																								voices_in_our_pc=engine.getProperty('voices')

																								engine.setProperty('rate',150)

																								engine.setProperty('voice',voices_in_our_pc[1].id)

																								engine.say("New information updated successfully")

																								engine.runAndWait()

																								update()

				btn6 = Button(ButtonFrame, text="Update", font=("arial", 20, "bold"), height=1, width=10,fg='#FF979E', bd=7,bg='#622227',relief = 'raise', command=uupdate)

				btn6.grid(row=0, column=5)

				def ieexit():

																								engine = pyttsx3.init()

																								rate = engine.getProperty('rate')

																								voices_in_our_pc=engine.getProperty('voices')

																								engine.setProperty('rate',150)

																								engine.setProperty('voice',voices_in_our_pc[1].id)

																								engine.say("Do you want to exit")

																								engine.runAndWait()

																								iexit()

				btn7 = Button(ButtonFrame, text="Exit", font=("arial", 20, "bold"), height=1,fg='#FF979E',bg='#622227', width=10, bd=7, command=ieexit ,relief = 'raise')

				btn7.grid(row=0, column=6)

				r.mainloop()

			def doct():

				qk.destroy()

				r = Tk()

				r.iconbitmap(r"hms.ico")

				r.resizable(0, 0)

				r.title("HOSPITAL MANGEMENT SYSTEM")

				a0=ttk.Style()

				a0.theme_use('winnative')

				a0.configure( "TProgressbar",background='#FF979E' ,troughcolor ='gray10' )

				a=ttk.Progressbar(r,style='TProgressbar',orient='horizontal',length=800,mode='determinate')

				a.pack()

				status = Label(r, text="Click button to start process..",bg='light gray', relief=SUNKEN, anchor=W, bd=2)

				status.pack(side=BOTTOM, fill=X)

				a.start(400)

				status.config(text='Working on it ........')

				a['maximum']=1000

				for i in range(1001):

					a['value']=i

					a.update()

				a['value']=0

				a.stop()

				r.destroy()

				engine = pyttsx3.init()

				rate = engine.getProperty('rate')

				voices_in_our_pc=engine.getProperty('voices')

				engine.setProperty('rate',150)

				engine.setProperty('voice',voices_in_our_pc[1].id)

				engine.say("Now opening the doctor window")

				engine.runAndWait()   

				doctt()

			def deladmin():

				nam = StringVar()

				qk.destroy()

				admin0 = Tk()

				admin0.config(bg='gray10')

				admin0.iconbitmap(r"hms.ico")

				admin0.title("Delete Admin")         

				admin0.geometry("300x120")

				admin0.resizable(0, 0)

				name0 = Label(admin0,bg='gray10',fg='light green', text="Enter Admin to be deleted :")

				name0.place(x=10, y=10)

				nam0 = ttk.Entry(admin0, textvariable=nam)

				nam0.place(x=170, y=10)

				def deleteadmin():

					adm = nam0.get()

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					x = cur.execute("delete from UNLOCK_FOR_ADMIN where username = '%s'" %adm )

					cur.execute("commit")

					sentence = 'Admin ' + adm + ' , deleted successfully.'

					engine = pyttsx3.init()

					rate = engine.getProperty('rate')

					voices_in_our_pc=engine.getProperty('voices')

					engine.setProperty('rate',150)

					engine.setProperty('voice',voices_in_our_pc[1].id)

					engine.say(sentence)

					engine.runAndWait()

					messagebox.showinfo('Admin deleted', sentence)

				def canceell():

					admin0.destroy()

					fa()

				bn = Button(admin0,bg='green',fg='white', text="DELETE", width=37, command=deleteadmin,relief = 'raise' , bd = 7)

				bn.place(x=10, y=40)

				bn0 = Button(admin0,bg='green',fg='white', text='CANCEL', width=37, command=canceell,relief = 'raise',bd = 7)

				bn0.place(x=10, y=80)

			def deluser():

				nam = StringVar()

				qk.destroy()

				user0 = Tk()

				user0.config(bg='gray10')

				user0.iconbitmap(r"hms.ico")

				user0.title("Delete User")

				user0.geometry("300x120")

				user0.resizable(0, 0)

				name0 = Label(user0,bg='gray10',fg='light green', text="Enter User to be deleted :")

				name0.place(x=10, y=10)

				nam0 = ttk.Entry(user0, textvariable=nam)

				nam0.place(x=170, y=10)

				def deleteuser():

					adm = nam0.get()

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					x = cur.execute("delete from UNLOCK_FOR_USER where username = '%s'" %adm )

					cur.execute("commit")

					sentence = 'User ' + adm + ' , deleted successfully.'

					engine = pyttsx3.init()

					rate = engine.getProperty('rate')

					voices_in_our_pc=engine.getProperty('voices')

					engine.setProperty('rate',150)

					engine.setProperty('voice',voices_in_our_pc[1].id)

					engine.say(sentence)

					engine.runAndWait()

					messagebox.showinfo('User deleted', sentence)

				def canceelll():

					user0.destroy()

					fa()

				bn = Button(user0,bg='green',fg='white', text="DELETE", width=37, command=deleteuser,relief = 'raise' , bd = 7)

				bn.place(x=10, y=40)

				bn0 = Button(user0,bg='green',fg='white', text='CANCEL', width=37, command=canceelll,relief = 'raise' , bd = 7)

				bn0.place(x=10, y=80)

			def addadmin():

				nam = StringVar()


				paso= StringVar()

				qk.destroy()

				admin = Tk()

				admin.config(bg='gray10')

				admin.iconbitmap(r"hms.ico")

				admin.title("Add Admin")

				admin.geometry("260x180")

				admin.resizable(0, 0)


				name0 = Label(admin,bg='gray10',fg='cyan', text="Enter Admin Name :")

				name0.place(x=10, y=10)

				nam0 = ttk.Entry(admin,textvariable=nam)

				nam0.place(x=120, y=10)

				pass0 = Label(admin,bg='gray10',fg='cyan', text="Enter Password :")

				pass0.place(x=10, y=40)

				pas0 = ttk.Entry(admin, show="*")

				pas0.place(x=120, y=40)

				pass1 = Label(admin,bg='gray10',fg='cyan', text="Confirm Password :")


				pass1.place(x=10, y=70)

				pas1 = ttk.Entry(admin, show="*",textvariable = paso)

				pas1.place(x=120, y=70)


				def cancell():

					admin.destroy()

					fa()

					return

				def newadmin():

					newwn = nam0.get()

					newp = pas1.get()

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()


					x = cur.execute("insert into UNLOCK_FOR_ADMIN values('%s' , '%s')"%(newwn , newp))

					cur.execute("commit")

					sentence= 'New admin ' +newwn+  ' , added successfully.'

					engine = pyttsx3.init()

					rate = engine.getProperty('rate')

					voices_in_our_pc=engine.getProperty('voices')

					engine.setProperty('rate',150)

					engine.setProperty('voice',voices_in_our_pc[1].id)

					engine.say(sentence)

					engine.runAndWait()

					messagebox.showinfo('Admin added',sentence)

				bn = Button(admin,bg='cadet blue',fg='white', text="ADD", width=32, command=newadmin,relief = 'raise' , bd = 7)


				bn.place(x=10, y=100)

				bn0 = Button(admin,bg='cadet blue',fg='white', text='CANCEL', width=32, command=cancell,relief = 'raise' , bd = 7)

				bn0.place(x=10, y=140)

				return

			def adduser():


				nam = StringVar()

				paso = StringVar()

				qk.destroy()

				user = Tk()

				user.config(bg='gray10')


				user.iconbitmap(r"hms.ico")

				user.title("Add User")

				user.geometry("260x180")

				user.resizable(0, 0)

				name0 = Label(user,bg='gray10',fg='cyan', text="Enter User Name :")

				name0.place(x=10, y=10)

				nam0 = ttk.Entry(user, textvariable=nam)

				nam0.place(x=120, y=10)

				pass0 = Label(user,bg='gray10',fg='cyan', text="Enter Password :")

				pass0.place(x=10, y=40)

				pas0 = ttk.Entry(user, show="*")

				pas0.place(x=120, y=40)


				pass1 = Label(user,bg='gray10',fg='cyan', text="Confirm Password :")

				pass1.place(x=10, y=70)

				pas1 = ttk.Entry(user, show="*", textvariable=paso)

				pas1.place(x=120, y=70)

				def cancelll():

					user.destroy()

					fa()


					return

				def newuser():

					newwn = nam0.get()

					newp = pas1.get()

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					x = cur.execute("insert into UNLOCK_FOR_USER values('%s' , '%s')" % (newwn, newp))


					cur.execute("commit")

					sentence = 'New user ' + newwn + ' , added successfully.'

					engine = pyttsx3.init()

					rate = engine.getProperty('rate')

					voices_in_our_pc=engine.getProperty('voices')

					engine.setProperty('rate',150)

					engine.setProperty('voice',voices_in_our_pc[1].id)

					engine.say(sentence)

					engine.runAndWait()

					messagebox.showinfo('User added', sentence)


					return

				bn = Button(user,bg='cadet blue',fg='white', text="ADD", width=32,command = newuser,relief = 'raise' , bd = 7)

				bn.place(x=10, y=100)

				bn0 = Button(user,bg='cadet blue',fg='white',text= 'CANCEL',width=32,command = cancelll,relief = 'raise' , bd = 7)

				bn0.place(x=10,y=140)

			def gooto():

				patient = Tk()

				patient.geometry("1365x740")


				patient.config(bg="gray10")

				patient.title("Hospital Mangement System")

				patient.iconbitmap(r"hms.ico")

				PatID = IntVar()

				Name = StringVar()

				Disease = StringVar()


				City = StringVar()

				Height = StringVar()

				Age = StringVar()


				Gender = StringVar()


				Address = StringVar()

				Mobile = StringVar()

				AppointmentNo = StringVar()


				Weight = StringVar()

				Bloodgroup = StringVar()

				m = Frame(patient)


				m.pack()

				c = Canvas(m, width=1365, height=704)

				c.pack()


				p = PhotoImage(file=r"hms11.png")

				c.create_image(0, 0, image=p, anchor="nw")


				Title = Label(m, font=('castellar', 35, 'bold'), text="Hospital  Mangement  System", fg="light green",bg="#799181", bd=7, anchor="w",relief="raise")

				Title.place(x=250,y=10)

				LeftFrametop=Frame(m, bd=8, relief="raise",bg="#799181",width = 841, height = 268)


				LeftFrametop.place(x=0,y=165)

				LeftFramebottomleft=Frame(m, width=405, height=207, bd=8, relief="raise",bg="#799181")

				LeftFramebottomleft.place(x=0,y=468)


				LeftFramebottomright=Frame(m, width=405, height=207, bd=8, relief="raise",bg="#799181")

				LeftFramebottomright.place(x=442,y=468)

				ScrollFrame=Frame(m, width=603,bg="#799181", height=200, bd=8, relief="raise")


				ScrollFrame.place(x=940 ,y= 165)

				ButtonFrame=Frame(m, width=295, height=400, bd=8, relief="raise",bg="light green")
				ButtonFrame.place(x= 940,y= 500)

				ButtonFrame2=Frame(m, width=295, height=400, bd=8, relief="raise",bg="light green")


				ButtonFrame2.place(x= 940,y= 625)

				lblPatID = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient ID",width = 15,bg="#799181", fg="light green", bd=7, relief="ridge")

				lblPatID.place(x=0,y=20)

				txtPatID = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="#BCECCC",fg='green', justify="center", textvariable = PatID, relief="ridge")


				txtPatID.place(x=200 , y=20)

				lblname = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient Name",bg="#799181", fg="light green", bd=7, relief="ridge",width = 15)

				lblname.place(x=0,y=80)

				txtname = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="#BCECCC",fg='green', justify="center", textvariable = Name, relief="ridge")

				txtname.place(x=200 , y=80)

				lblAddress = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Address",bg="#799181", fg="light green", bd=7, relief="ridge",width = 15)

				lblAddress.place(x=0 , y=140)


				txtAddress = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="#BCECCC",fg='green', justify="center", textvariable = Address, relief="ridge")

				txtAddress.place(x=200 , y=140)

				lblAppointmentNo = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Appointment No.",bg="#799181", fg="light green", bd=7, relief="ridge",width = 15)


				lblAppointmentNo.place(x=0 , y=200)

				txtAppointmentNo = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="#BCECCC",fg='green', justify="center", textvariable = AppointmentNo, relief="ridge")

				txtAppointmentNo .place(x=200 , y=200)

				lblCity = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="City",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)

				lblCity.place(x=0,y=0)

				txtCity = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = City, relief="ridge")

				txtCity.place(x=175,y=0)

				lblHeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Height (cms)",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)


				lblHeight.place(x=0,y=50)

				txtHeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = Height, relief="ridge")

				txtHeight.place(x=175,y=50)


				lblgender = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Gender",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)

				lblgender.place(x=0,y=100)


				gen=['Male','Female'];

				txtgender = OptionMenu(LeftFramebottomleft,Gender,*gen)


				txtgender.config(relief="ridge",font=('arial', 14, 'bold'), bd=4, width=15, bg="#BCECCC",fg='green', justify="center")

				txtgender.place(x=175,y=100)


				lblWeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Weight (kgs)",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)

				lblWeight.place(x=0,y=150)


				txtWeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = Weight, relief="ridge")

				txtWeight.place(x=175,y=150)

				lblage = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Age (yrs) ",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)

				lblage.place(x=0,y=0)

				txtage = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = Age, relief="ridge")


				txtage.place(x=175,y=0)

				lblmobile = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Mobile number",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)


				lblmobile.place(x=0,y=50 )


				txtmobile = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = Mobile, relief="ridge")

				txtmobile.place(x=175,y=50)


				lbldisease = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Disease",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)

				lbldisease.place(x=0,y=100)

				txtdisease = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = Disease, relief="ridge")

				txtdisease.place(x=175,y=100)

				lblbldgrp = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Blood Group",bg="#799181", fg="light green", bd=7, relief="ridge",width = 13)
			
				lblbldgrp.place(x=0,y=150)

				txtbldgrp = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="#BCECCC",fg='green', justify="center", textvariable = Bloodgroup, relief="ridge")

				txtbldgrp.place(x=175,y=150)

				def  iexit():

					iexit = messagebox.askokcancel("Hospital Managment System"," Do you want to exit ")

					if  iexit > 0:

						patient.destroy ()

						fa()

						return

				def cleardata():

					txtPatID.delete(0,END)

					txtname.delete(0,END)

					txtage.delete(0,END)

					txtCity.delete(0,END)

					txtdisease.delete(0,END)

					txtAddress.delete(0,END)

					txtAppointmentNo.delete(0,END)

					txtHeight.delete(0,END)

					txtmobile.delete(0,END)

					txtWeight.delete(0,END)

					txtbldgrp.delete(0,END)

					Gender.set('')

				def addrecorddoc(a, b, c, d, e, f, g,  h ,i , j , k , l):
								
								conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

								cur = conn.cursor()

								cur.execute("insert into PATIENT_RECORD values (%d , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (a, b, c, d, e, f, g,  h ,i , j , k , l))

								cur.execute("commit")

								conn.close

				def adddata():

								addrecorddoc(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

								patlist.delete(0, END)

								patlist.insert(END, (
								
								txtPatID.get() , txtname.get(),txtdisease.get(),txtbldgrp.get(), AppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()),)
							   
								messagebox.showinfo('Hospital Mangement System','New Patient Added Successfully')
			   
				def viewdata():
						   
							conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')
						   
							cur = conn.cursor()
						   
							cur.execute("select * from PATIENT_RECORD")
						   
							row = cur.fetchall()
						   
							conn.close
						   
							return row
			   
				def displaydata():
   
							patlist.delete(0, END)

							for row in viewdata():

								patlist.insert(END, row, str(" "))

				def PATIENT_RECORD(event):


					global sd
				   
					searchpat = patlist . curselection() [0]

					sd = patlist . get( searchpat )

					txtPatID.delete(0,END)

					txtPatID.insert(END,sd[0])

					txtbldgrp.delete(0,END)

					txtbldgrp.insert(END,sd[3])

					txtWeight.delete(0,END)

					txtWeight.insert(END,sd[8])

					txtHeight.delete(0,END)

					txtHeight.insert(END,sd[9])

					txtAppointmentNo.delete(0,END)

					txtAppointmentNo.insert(END,sd[4])

					txtname.delete(0,END)

					txtname.insert(END,sd[1])


					txtage.delete(0,END)

					txtage.insert(END,sd[5])

					Gender.set('')

					Gender.set(sd[6])

					txtCity.delete(0,END)

					txtCity.insert(END,sd[7])

					txtdisease.delete(0,END)

					txtdisease.insert(END,sd[2])

					txtAddress.delete(0,END)


					txtAddress.insert(END,sd[10])

					txtmobile.delete(0,END)

					txtmobile.insert(END,sd[11])

				def deleterec(patid):

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					cur.execute("delete  from PATIENT_RECORD where patid = %d" % patid)

					cur.execute("commit")

					conn.close

				def deletedata():

					searchpat = patlist.curselection()[0]

					sd = patlist.get(searchpat)

					deleterec(sd[0])

					cleardata()

					displaydata()

					messagebox.showinfo('Hospital Mangement System', ' Patient Deleted Successfully')

				def ssearchdata(x):

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					cur.execute("select * from PATIENT_RECORD where patid = %d  " % x)

					row = cur.fetchall()

					conn.close

					return row

				def searchdata():

					patlist.delete(0, END)

					for row in ssearchdata(int(txtPatID.get())):

						cleardata()

						patlist.insert(END, row, str(""))

						x00=row[0]

						x=row[1]

						x0=row[4]

						x1=row[2]

						x3=row[3]

						x4=row[5]

						x5=row[6]

						x6=row[7]

						x7=row[8]

						x8=row[9]

						x9=row[10]

						x10=row[11]

						txtPatID.insert(0,x00)

						txtCity.insert(0,x6)

						Gender.set(x5)

						txtage.insert(0,x4)

						txtbldgrp.insert(0,x3)

						txtdisease.insert(0,x1)

						txtAppointmentNo.insert(0,x0)

						txtname.insert(0,x)

						txtWeight.insert(0,x7)

						txtHeight.insert(0,x8)

						txtAddress.insert(0,x9)

						txtmobile.insert(0,x10)
				def dtr():

					patient.destroy()

					win = Tk()

					win.resizable(0,0)

					win.config(bg='gray10')

					win.title('Showing all doctors')


					win.iconbitmap(r"hms.ico")

					win.geometry("900x500")

					DataFrameLEFT = LabelFrame(win, width=100, height=700, bd=1, padx=20, pady=3, bg="light green",fg='green', relief=RIDGE, text="Doctor Name\n", font=('impact', 20))

					DataFrameLEFT.grid(row=0,column=0)

					DataFrameRIGHT = LabelFrame(win, bd=1, width=100, height=700, padx=31, pady=3, bg="#799181",fg='light green', relief=RIDGE, text="Speciality in Disease \n", font=('impact', 20))

					DataFrameRIGHT.grid(row=0,column=1)

					scr = Scrollbar(DataFrameLEFT)

					scr.grid(row=0, column=1, sticky='NS')

					pa = Listbox(DataFrameLEFT, width=28, height=16,fg='green',bg='light gray', font=("castellar", 12, "bold"), yscrollcommand=scr.set)

					pa.grid(row=0, column=0)

					scr.config(command=pa.yview)

					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur = conn.cursor()

					x = cur.execute("select  name from DOCTOR_RECORD")

					for row in x:

						pa.insert(END, row, '\n')

					scr2 = Scrollbar(DataFrameRIGHT)

					scr2.grid(row=0, column=1, sticky='NS')

					pa2= Listbox(DataFrameRIGHT, width=28, height=16,fg='light green',bg='gray10', font=("castellar", 12, "bold"), yscrollcommand=scr.set)


					pa2.grid(row=0, column=0)

					scr2.config(command=pa2.yview)

					con = cx_Oracle.connect(f'system/{orname.get()}@localhost')

					cur0 = con.cursor()

					y = cur0.execute("select  specialist from DOCTOR_RECORD")

					for i in y:

						pa2.insert(END, i , '\n')

					def cing():

						win.destroy()

						goto()

					Button(win, text='CANCEL', font=("algerian", 15,'italic'), command=cing, width=20,bd=7,relief='raise',bg='dark green',fg='white').place(x=320,y=420)

					win.mainloop()

				def update():

					searchpat = patlist.curselection()[0]

					sd = patlist.get(searchpat)

					patlist.delete(0, END)

					deleterec(sd[0])



					addrecorddoc(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

					patlist.delete(0, END)

					patlist.insert(END, (

					int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()))

					messagebox.showinfo('Hospital Mangement System', 'New Information Updated Successfully')

				scroll=Scrollbar(ScrollFrame)

				scroll.grid(row=0,column=1,sticky='NS')

				patlist=Listbox(ScrollFrame,   width=42,  height=16,font=("arial",12,"bold"), yscrollcommand=scroll.set ,fg='green',bg='#BCECCC')

				patlist.bind('<<ListboxSelect>>',PATIENT_RECORD)

				patlist.grid(row=0,column=0,  padx=8)

				scroll.config(command = patlist.yview)

				def aadddata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("New patient added successfully")

																						  engine.runAndWait()

																						  adddata()


				btn1 = Button(ButtonFrame, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=8, bd=7,

				text="Add New", bg="#799181", command=aadddata, relief="raise").grid(row=0, column=0)

				def ddisplaydata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Displaying all the existing patients")

																						  engine.runAndWait()

																						  displaydata()

				btn2 = Button(ButtonFrame, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=8, bd=7,

				text="Display", bg="#799181", command=ddisplaydata, relief="raise").grid(row=0, column=1)

				btn3 = Button(ButtonFrame, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=8, bd=7,

				text="Search", bg="#799181", command=searchdata, relief="raise").grid(row=0, column=2)

				def ccleardata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("This will clear all the entry fields")

																						  engine.runAndWait()

																						  cleardata()

				btn4 = Button(ButtonFrame, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=8, bd=7,

				text="Clear", bg="#799181", command=ccleardata, relief="raise").grid(row=1, column=0)

				def det():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Patient deleted successfully")

																						  engine.runAndWait()

																						  deletedata()

				btn5 = Button(ButtonFrame, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=8, bd=7,

				text="Delete", bg="#799181", command=det, relief="raise").grid(row=1, column=1)

				def uupdate():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("New Information Updated Successfully")

																						  engine.runAndWait()

																						  update()

				btn6 = Button(ButtonFrame, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=8, bd=7,

				text="Update", bg="#799181", command=uupdate, relief="raise").grid(row=1, column=2)

				def ddtr():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Showing all the available doctors")

																						  engine.runAndWait()

																						  dtr()

				btn7 = Button(ButtonFrame2, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=13, bd=7,

				text="Doctors", bg="#799181", command=ddtr, relief="raise").grid(row=2, column=0)

				def ieexit():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Do you want to exit")

																						  engine.runAndWait()

																						  iexit()

				btn8 = Button(ButtonFrame2, padx=8, pady=8, fg="light green", font=('castellar', 12, 'bold'), width=14, bd=7,

				text="Exit", bg="#799181", command=ieexit, relief="raise").grid(row=2, column=1)

				patient.mainloop()

			def goto():

				r = Tk()

				r.iconbitmap(r"hms.ico")

				r.resizable(0, 0)

				r.title("HOSPITAL MANGEMENT SYSTEM")

				a0=ttk.Style()

				a0.theme_use('winnative')

				a0.configure( "TProgressbar",background='light green' ,troughcolor ='gray10' )

				a=ttk.Progressbar(r,style='TProgressbar',orient='horizontal',length=800,mode='determinate')

				a.pack()

				status = Label(r, text="Click button to start process..",bg='light gray', relief=SUNKEN, anchor=W, bd=2)

				status.pack(side=BOTTOM, fill=X)

				a.start(400)

				status.config(text='Working on it ........')

				a['maximum']=1000

				for i in range(1001):

					a['value']=i

					a.update()

				a['value']=0

				a.stop()

				r.destroy()

				engine = pyttsx3.init()

				rate = engine.getProperty('rate')

				voices_in_our_pc=engine.getProperty('voices')

				engine.setProperty('rate',150)

				engine.setProperty('voice',voices_in_our_pc[1].id)

				engine.say("Now opening the patient window")

				engine.runAndWait()   

				gooto()

			def shadmin():

				engine = pyttsx3.init()

				rate = engine.getProperty('rate')

				voices_in_our_pc=engine.getProperty('voices')

				engine.setProperty('rate',150)

				engine.setProperty('voice',voices_in_our_pc[1].id)

				engine.say("Showing all the available administrators")

				engine.runAndWait()

				win = Tk()

				win.config(bg='gray10')

				win.title ('Showing all administrators')

				win.iconbitmap(r"hms.ico")

				win.geometry("400x400")

				scr = Scrollbar(win)

				scr.grid(row=0, column=1, sticky='NS')

				pa = Listbox(win, width=41, height=16,fg='maroon',bg='light gray', font=("castellar", 12, "bold"), yscrollcommand=scr.set)


				pa.grid(row=0, column=0, padx=8)

				scr.config(command=pa.yview)

				conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

				cur = conn.cursor()

				x = cur.execute("select  username from UNLOCK_FOR_ADMIN")

				for row in x:

					pa.insert(END, row, '\n')

				def cing():

					win.destroy()

					fa()

				Button(win,text = 'CANCEL',command = cing , width = 30,bd=7,relief='raise',bg='maroon',fg='white').grid(row = 2,column = 0)

				win . mainloop()

			def shuser():                                
		
				engine = pyttsx3.init()

				rate = engine.getProperty('rate')

				voices_in_our_pc=engine.getProperty('voices')

				engine.setProperty('rate',150)

				engine.setProperty('voice',voices_in_our_pc[1].id)

				engine.say("Showing all the available users")

				engine.runAndWait()

				win = Tk()

				win.config(bg='gray10')

				win.title('Showing all users')

				win.iconbitmap(r"hms.ico")

				win.geometry("400x400")

				scr = Scrollbar(win)

				scr.grid(row=0, column=1, sticky='NS')

				pa = Listbox(win, width=41, height=16,fg='maroon',bg='light gray', font=("castellar", 12, "bold"), yscrollcommand=scr.set)

				pa.grid(row=0, column=0, padx=8)

				scr.config(command=pa.yview)

				conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

				cur = conn.cursor()

				x = cur.execute("select  username from UNLOCK_FOR_USER")

				for row in x:

					pa.insert(END, row, '\n')

				def cing():

					win.destroy()

					fa()

				Button(win, text='CANCEL', command=cing, width=30,bd=7,relief='raise',bg='maroon',fg='white').grid(row = 2,column = 0)

				win.mainloop()

			def iex():

				qk.destroy()

				r = Tk()

				r.iconbitmap(r"hms.ico")

				r.resizable(0, 0)

				r.title("HOSPITAL MANGEMENT SYSTEM")

				a=ttk.Progressbar(r,style='TProgressbar',orient='horizontal',length=1000,mode='determinate')

				a.pack()

				status = Label(r, text="Click button to start process..",bg='light gray', relief=SUNKEN, anchor=W, bd=2)

				status.pack(side=BOTTOM, fill=X)

				a.start()

				status.config(text='Working on it ........')

				a['maximum']=1000

				for i in range(1001):

					a['value']=i

					a.update()

				a['value']=0

				a.stop()

				r.destroy()

				main()

			sen = 'Welcome Mr. ' + usser + '\n  you have logged in successfully'

			engine=pyttsx3.init()

			rate = engine.getProperty('rate')

			voices_in_our_pc=engine.getProperty('voices')

			engine.setProperty('rate',150)

			engine.setProperty('voice',voices_in_our_pc[1].id)

			engine.say(sen)

			engine.say("Choose What do you want to perform")

			engine.runAndWait()

			qk=Tk()

			qk.title("ADMINISITRATOR")

			qk.iconbitmap(r"hms.ico")

			qk.resizable(0,0)

			qk.config(bg='gray10')

			qk.geometry("350x460")

			Label(qk,text=sen,bg='gray10',fg='white', font=('castellar', 10, 'bold','italic')).pack()

			bt0=Button(qk,bg='maroon',fg='white',text='Add New Administrator',command = addadmin,width = 30,relief='raise',bd=7,font=('calibri',10,'bold'))

			bt0.place(x=70,y=50)

			bt1=Button(qk,bg='maroon',fg='white',text='Add New User',width = 30,command = adduser,relief='raise',bd=7,font=('calibri',10,'bold'))

			bt1.place(x=70,y=95)

			bt2 =Button(qk, text='Doctors',bg='maroon',fg='white',command=doct,width = 30,relief='raise',font=('calibri',10,'bold'),bd=7)

			bt2.place(x=70,y=140)

			def got():

				qk.destroy()

				goto()

			bt3 =Button(qk, text='Patients',command=got,bg='maroon',fg='white',width = 30,relief='raise',font=('calibri',10,'bold'),bd=7)

			bt3.place(x=70,y=185)

			bt4 = Button(qk, text='Delete administrator', command=deladmin,bg='maroon',font=('calibri',10,'bold'),fg='white',width=30,relief='raise',bd=7)

			bt4.place(x=70,y=230)

			bt5 = Button(qk, text='Delete user', command = deluser ,font=('calibri',10,'bold'),bg='maroon',fg='white',width=30,relief='raise',bd=7)

			bt5.place(x=70,y=275)

			def sshadmin():

																																																																							qk.destroy()

																																																																							shadmin()

			bt6 = Button(qk, text='Show all administrators',font=('calibri',10,'bold'), command=sshadmin,bg='maroon',fg='white', width=30,relief='raise',bd=7)

			bt6.place(x=70,y=320)

			def sshuser():

																qk.destroy()

																shuser()

			bt7 = Button(qk, text='Show all users', command=sshuser,font=('calibri',10,'bold'),bg='maroon',fg='white',width=30,relief='raise',bd=7)

			bt7.place(x=70,y=365)

			bt8 =Button(qk, text = 'Exit', command=iex,bg='maroon',font=('calibri',10,'bold'),fg='white',width = 30,relief='raise',bd=7)

			bt8.place(x=70,y=410)

			qk.mainloop()

			

		def fuu():

			patient = Tk()

			patient.geometry("1365x740")

			patient.config(bg="gray10")

			patient.title("Hospital Mangement System")

			patient.iconbitmap(r"hms.ico")

			PatID = IntVar()

			Name = StringVar()

			Disease = StringVar()

			City = StringVar()

			Height = StringVar()

			Age = StringVar()

			Gender = StringVar()

			Address = StringVar()

			Mobile = StringVar()

			AppointmentNo = StringVar()

			Weight = StringVar()

			Bloodgroup = StringVar()

			m = Frame(patient)

			m.pack()

			c = Canvas(m, width=1365, height=704)

			c.pack()

			p = PhotoImage(file=r"hms10.png")

			c.create_image(0, 0, image=p, anchor="nw")

			Title = Label(m, font=('castellar', 35, 'bold'), text="Hospital  Mangement  System", fg="cyan",bg="#006170", bd=7, anchor="w",relief="raise")

			Title.place(x=250,y=10)

			LeftFrametop=Frame(m, bd=8, relief="raise",bg="#006170",width = 841, height = 268)

			LeftFrametop.place(x=0,y=165)

			LeftFramebottomleft=Frame(m, width=405, height=207, bd=8, relief="raise",bg="#006170")

			LeftFramebottomleft.place(x=0,y=468)

			LeftFramebottomright=Frame(m, width=405, height=207, bd=8, relief="raise",bg="#006170")

			LeftFramebottomright.place(x=442,y=468)

			ScrollFrame=Frame(m, width=603, height=200,bg="#006170", bd=8, relief="raise")

			ScrollFrame.place(x=940 ,y= 165)

			ButtonFrame=Frame(m, width=295, height=400, bd=8, relief="raise",bg="powder blue")

			ButtonFrame.place(x= 940,y= 500)

			ButtonFrame2=Frame(m, width=295, height=400, bd=8, relief="raise",bg="powder blue")

			ButtonFrame2.place(x= 940,y= 625)

			lblPatID = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient ID",width = 15,bg="#006170", fg="cyan", bd=7, relief="ridge")

			lblPatID.place(x=0,y=20)

			txtPatID = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = PatID, relief="ridge")

			txtPatID.place(x=200 , y=20)

			lblname = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Patient Name",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 15)

			lblname.place(x=0,y=80)

			txtname = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Name, relief="ridge")

			txtname.place(x=200 , y=80)

			lblAddress = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Address",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 15)

			lblAddress.place(x=0 , y=140)

			txtAddress = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Address, relief="ridge")

			txtAddress.place(x=200 , y=140)

			lblAppointmentNo = Label(LeftFrametop, font=('bell mt', 14, 'bold'), text="Appointment No.",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 15)

			lblAppointmentNo.place(x=0 , y=200)

			txtAppointmentNo = Entry(LeftFrametop, font=('arial', 14, 'bold'), bd=12, width=54, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = AppointmentNo, relief="ridge")

			txtAppointmentNo .place(x=200 , y=200)

			lblCity = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="City",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblCity.place(x=0,y=0)

			txtCity = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = City, relief="ridge")

			txtCity.place(x=175,y=0)

			lblHeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Height (cms)",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblHeight.place(x=0,y=50)

			txtHeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Height, relief="ridge")

			txtHeight.place(x=175,y=50)


			lblgender = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Gender",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblgender.place(x=0,y=100)

			gen=['Male','Female'];

			txtgender = OptionMenu(LeftFramebottomleft,Gender,*gen)


			txtgender.config(relief="ridge",font=('arial', 14, 'bold'), bd=4, width=15, bg="powder blue",fg = '#3F7C7C', justify="center")

			txtgender.place(x=175,y=100)

			lblWeight = Label(LeftFramebottomleft, font=('bell mt', 14, 'bold'), text="Weight (kgs)",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblWeight.place(x=0,y=150)

			txtWeight = Entry(LeftFramebottomleft,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Weight, relief="ridge")

			txtWeight.place(x=175,y=150)

			lblage = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Age (yrs) ",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblage.place(x=0,y=0)

			txtage = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Age, relief="ridge")

			txtage.place(x=175,y=0)

			lblmobile = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Mobile number",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblmobile.place(x=0,y=50 )

			txtmobile = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Mobile, relief="ridge")

			txtmobile.place(x=175,y=50)

			lbldisease = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Disease",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lbldisease.place(x=0,y=100)

			txtdisease = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Disease, relief="ridge")

			txtdisease.place(x=175,y=100)

			lblbldgrp = Label(LeftFramebottomright, font=('bell mt', 14, 'bold'), text="Blood Group",bg="#006170", fg="cyan", bd=7, relief="ridge",width = 13)

			lblbldgrp.place(x=0,y=150)

			txtbldgrp = Entry(LeftFramebottomright,font=('arial', 14, 'bold'), bd=7, width=18, bg="powder blue",fg = '#3F7C7C', justify="center", textvariable = Bloodgroup, relief="ridge")

			txtbldgrp.place(x=175,y=150)

			def  iexit():

				iexit = messagebox.askokcancel("Hospital Managment System"," Do you want to exit ")

				if  iexit > 0:

					patient.destroy ()

					r = Tk()

					r.iconbitmap(r"hms.ico")

					r.resizable(0, 0)

					r.title("HOSPITAL MANGEMENT SYSTEM")

					a=ttk.Progressbar(r,style='TProgressbar',orient='horizontal',length=1000,mode='determinate')

					a.pack()

					status = Label(r, text="Click button to start process..",bg='light gray', relief=SUNKEN, anchor=W, bd=2)

					status.pack(side=BOTTOM, fill=X)

					a.start()

					status.config(text='Working on it ........')

					a['maximum']=1000

					for i in range(1001):

						a['value']=i

						a.update()

					a['value']=0

					a.stop()

					r.destroy()

					main()

					return

			def cleardata():

				txtPatID.delete(0,END)

				txtname.delete(0,END)

				txtage.delete(0,END)

				txtCity.delete(0,END)

				txtdisease.delete(0,END)

				txtAddress.delete(0,END)

				txtAppointmentNo.delete(0,END)

				txtHeight.delete(0,END)

				txtmobile.delete(0,END)

				txtWeight.delete(0,END)

				txtbldgrp.delete(0,END)

				Gender.set('')

			def addrecorddoc(a, b, c, d, e, f, g,  h ,i , j , k , l):

							conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

							cur = conn.cursor()

							cur.execute("insert into PATIENT_RECORD values (%d , '%s' ,'%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s' , '%s')" % (a, b, c, d, e, f, g,  h ,i , j , k , l))

							cur.execute("commit")

							conn.close

			def adddata():

							addrecorddoc(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

							patlist.delete(0, END)

							patlist.insert(END, (

							txtPatID.get() , txtname.get(),txtdisease.get(),txtbldgrp.get(), AppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()),)

							messagebox.showinfo('Hospital Mangement System','New Patient Added Successfully')

			def viewdata():

						conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

						cur = conn.cursor()

						cur.execute("select * from PATIENT_RECORD")

						row = cur.fetchall()

						conn.close

						return row

			def displaydata():

						patlist.delete(0, END)

						for row in viewdata():

							patlist.insert(END, row, str(" "))

			def PATIENT_RECORD(event):

				global sd

				searchpat = patlist . curselection() [0]

				sd = patlist . get( searchpat )

				txtPatID.delete(0,END)

				txtPatID.insert(END,sd[0])

				txtbldgrp.delete(0,END)

				txtbldgrp.insert(END,sd[3])

				txtWeight.delete(0,END)

				txtWeight.insert(END,sd[8])

				txtHeight.delete(0,END)

				txtHeight.insert(END,sd[9])

				txtAppointmentNo.delete(0,END)

				txtAppointmentNo.insert(END,sd[4])

				txtname.delete(0,END)

				txtname.insert(END,sd[1])

				txtage.delete(0,END)

				txtage.insert(END,sd[5])

				Gender.set('')

				Gender.set(sd[6])

				txtCity.delete(0,END)

				txtCity.insert(END,sd[7])

				txtdisease.delete(0,END)

				txtdisease.insert(END,sd[2])

				txtAddress.delete(0,END)

				txtAddress.insert(END,sd[10])

				txtmobile.delete(0,END)

				txtmobile.insert(END,sd[11])

			def deleterec(patid):

				conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

				cur = conn.cursor()

				cur.execute("delete  from PATIENT_RECORD where patid = %d" % patid)

				cur.execute("commit")

				conn.close

			def deletedata():

				searchpat = patlist.curselection()[0]

				sd = patlist.get(searchpat)

				deleterec(sd[0])

				cleardata()

				displaydata()

				messagebox.showinfo('Hospital Mangement System', ' Patient Deleted Successfully')

			def ssearchdata(x):

				conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

				cur = conn.cursor()

				cur.execute("select * from PATIENT_RECORD where patid = %d  " % x)

				row = cur.fetchall()

				conn.close

				return row

			def searchdata():

				patlist.delete(0, END)

				for row in ssearchdata(int(txtPatID.get())):

					cleardata()

					patlist.insert(END, row, str(""))

					x00=row[0]

					x=row[1]

					x0=row[4]

					x1=row[2]

					x3=row[3]

					x4=row[5]

					x5=row[6]

					x6=row[7]

					x7=row[8]

					x8=row[9]

					x9=row[10]

					x10=row[11]

					txtPatID.insert(0,x00)

					txtCity.insert(0,x6)

					Gender.set(x5)

					txtage.insert(0,x4)

					txtbldgrp.insert(0,x3)

					txtdisease.insert(0,x1)

					txtAppointmentNo.insert(0,x0)

					txtname.insert(0,x)

					txtWeight.insert(0,x7)

					txtHeight.insert(0,x8)

					txtAddress.insert(0,x9)

					txtmobile.insert(0,x10)



			def dtr():

				patient.destroy()

				win = Tk()

				win.resizable(0,0)

				win.config(bg='gray10')

				win.title('Showing all doctors')

				win.iconbitmap(r"hms.ico")

				win.geometry("900x500")

				DataFrameLEFT = LabelFrame(win, width=100, height=700, bd=1, padx=20, pady=3, bg="#71D4F2",fg='#006170', relief=RIDGE, text="Doctor Name\n", font=('impact', 20))

				DataFrameLEFT.grid(row=0,column=0)

				DataFrameRIGHT = LabelFrame(win, bd=1, width=100, height=700, padx=31, pady=3, bg="#006170",fg='#71D4F2', relief=RIDGE, text="Speciality in Disease \n", font=('impact', 20))

				DataFrameRIGHT.grid(row=0,column=1)

				scr = Scrollbar(DataFrameLEFT)

				scr.grid(row=0, column=1, sticky='NS')

				pa = Listbox(DataFrameLEFT, width=28, height=16,fg='#006170',bg='light gray', font=("castellar", 12, "bold"), yscrollcommand=scr.set)

				pa.grid(row=0, column=0)

				scr.config(command=pa.yview)

				conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')

				cur = conn.cursor()

				x = cur.execute("select  name from DOCTOR_RECORD")

				for row in x:

					pa.insert(END, row, '\n')

				scr2 = Scrollbar(DataFrameRIGHT)

				scr2.grid(row=0, column=1, sticky='NS')

				pa2= Listbox(DataFrameRIGHT, width=28, height=16,fg='#71D4F2',bg='gray10', font=("castellar", 12, "bold"), yscrollcommand=scr.set)

				pa2.grid(row=0, column=0)

				scr2.config(command=pa2.yview)

				con = cx_Oracle.connect(f'system/{orname.get()}@localhost')

				cur0 = con.cursor()

				y = cur0.execute("select  specialist from DOCTOR_RECORD")

				for i in y:

					pa2.insert(END, i , '\n')

				def cing():

					win.destroy()

					fu()

				Button(win, text='CANCEL', font=("algerian", 15,'italic'), command=cing, width=20,bd=7,relief='raise',bg='#006170',fg='white').place(x=320,y=420)

				win.mainloop()

			def update():

				searchpat = patlist.curselection()[0]

				sd = patlist.get(searchpat)


				patlist.delete(0, END)

				deleterec(sd[0])

				addrecorddoc(int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()  )

				patlist.delete(0, END)

				patlist.insert(END, (

				int(txtPatID.get()), txtname.get(),txtdisease.get(),txtbldgrp.get(), txtAppointmentNo.get() , txtage.get() , Gender.get() ,txtCity.get() ,  txtWeight.get() ,txtHeight.get() , txtAddress.get() , txtmobile.get()))

				messagebox.showinfo('Hospital Mangement System', 'New Information Updated Successfully')

			scroll=Scrollbar(ScrollFrame)

			scroll.grid(row=0,column=1,sticky='NS')

			patlist=Listbox(ScrollFrame,fg='#3F7C7C',bg  = 'powder blue',   width=42,  height=16,font=("arial",12,"bold"), yscrollcommand=scroll.set )

			patlist.bind('<<ListboxSelect>>',PATIENT_RECORD)

			patlist.grid(row=0,column=0,  padx=8)

			scroll.config(command = patlist.yview)

			def aadddata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("New patient added successfully")

																						  engine.runAndWait()

																						  adddata()



	
			btn1 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,


					text="Add New", bg="#006170", command=aadddata, relief="raise").grid(row=0, column=0)
			def ddisplaydata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Displaying all the existing patient")

																						  engine.runAndWait()

																						  displaydata()



  
			btn2 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,

					text="Display", bg="#006170", command=ddisplaydata, relief="raise").grid(row=0, column=1)
  
			btn3 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,
  
					text="Search", bg="#006170", command=searchdata, relief="raise").grid(row=0, column=2)

			def ccleardata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("This will clear all the entry fields")

																						  engine.runAndWait()

																						  cleardata()



  

  
			btn4 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,
  
					text="Clear", bg="#006170", command=ccleardata, relief="raise").grid(row=1, column=0)
			def ddeletedata():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("patient deleted successfully")

																						  engine.runAndWait()

																						  deletedata()



  

  

  
			btn5 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,
  
					text="Delete", bg="#006170", command=ddeletedata, relief="raise").grid(row=1, column=1)

			def uupdate():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("New information updated successfully")

																						  engine.runAndWait()

																						  update()



  

  

  

  
			btn6 = Button(ButtonFrame, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=8, bd=7,
  
					text="Update", bg="#006170", command=uupdate, relief="raise").grid(row=1, column=2)

			def ddtr():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Sowing all available doctors")

																						  engine.runAndWait()

																						  dtr()



  

  

  

  

  
			btn7 = Button(ButtonFrame2, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=13, bd=7,
  
				text="Doctors", bg="#006170", command=ddtr, relief="raise").grid(row=0, column=0)
			def ieexit():

																						  engine = pyttsx3.init()

																						  rate = engine.getProperty('rate')

																						  voices_in_our_pc=engine.getProperty('voices')

																						  engine.setProperty('rate',150)

																						  engine.setProperty('voice',voices_in_our_pc[1].id)

																						  engine.say("Do you want to exit")

																						  engine.runAndWait()

																						  iexit()



  

  

  

  

  

			
			btn8 = Button(ButtonFrame2, padx=8, pady=8, fg="cyan", font=('castellar', 12, 'bold'), width=14, bd=7,
  
				text="Exit", bg="#006170", command=ieexit, relief="raise").grid(row=0, column=1)
  
			patient.mainloop()
  
		def fu():
  
			r = Tk()
  
			r.iconbitmap(r"hms.ico")
  
			r.resizable(0, 0)
  
			r.title("HOSPITAL MANGEMENT SYSTEM")
  
			a0=ttk.Style()
  
			a0.theme_use('default')
  
			a0.configure( "TProgressbar",background='#006170' ,troughcolor ='white' )
  
			a=ttk.Progressbar(r,style='TProgressbar',orient='horizontal',length=800,mode='determinate')
	 
			a.pack()
	 
			status = Label(r, text="Click button to start process..",bg='light gray', relief=SUNKEN, anchor=W, bd=2)
	 
			status.pack(side=BOTTOM, fill=X)
	 
			a.start(400)
	 
			status.config(text='Working on it ........')
	 
			a['maximum']=1000
	 
			for i in range(1001):
	 
				a['value']=i
	 
				a.update()
	 
			a['value']=0
	 
			a.stop()
	 
			r.destroy()

			engine = pyttsx3.init()

			rate = engine.getProperty('rate')

			voices_in_our_pc=engine.getProperty('voices')

			engine.setProperty('rate',150)

			engine.setProperty('voice',voices_in_our_pc[1].id)

			engine.say("Now opening the patient window")

			engine.runAndWait()

			fuu()

	 
		def vadmin():
	 
			
			mn=Tk()
	 
			mn.iconbitmap(r"hms.ico")
	 
			mn.title("LOG IN ADMIN")
	 
			mn.geometry("255x110")
	 
			mn.config(bg='gray10')
	 
			mn.resizable(0,0)
	 
			name=StringVar()
	 
			passc=StringVar()
	 
			e=Label(mn,bg='gray10',fg='yellow',text="Enter Admin Name :")
	 
			e.place(x=10,y=10)
	 
			q=ttk.Entry(mn,textvariable=name)
	 
			q.place(x=120,y=10)
	 
			p=Label(mn,bg='gray10',fg='yellow',text="Enter Password :")
	 
			p.place(x=10,y=40)
	 
			w=ttk.Entry(mn,textvariable=passc,show='*')
	 
			w.place(x=120,y=40)
	 
			def wa():
	 
				global usser
	 
				usser=q.get()
	 
				user=str(usser)
	 
				ppass=w.get()
	 
				try:
	 
					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')
	 
					cur = conn.cursor()
	 
					x = cur.execute("select  username from UNLOCK_FOR_ADMIN where pass = '%s' "%ppass)
	 
					for i in x:
	 
						pr=i
	 
					if pr == (usser,) :
	 
						mn.destroy()
	 
						fa()
	 
					else:
	 
	 
						def speak(my_message):

							engine = pyttsx3.init()

							rate = engine.getProperty('rate')
							voices_in_our_pc=engine.getProperty('voices')
							engine.setProperty('rate',150)
							engine.setProperty('voice',voices_in_our_pc[1].id)
							engine.say(my_message)
						  
							engine.runAndWait()

							messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")


						speak("you have entered wrong log-in creditionals")
	 
				except:
	 
																											def speak(my_message):

																															engine = pyttsx3.init()

																															rate = engine.getProperty('rate')
																															voices_in_our_pc=engine.getProperty('voices')
																															engine.setProperty('rate',150)
																															engine.setProperty('voice',voices_in_our_pc[1].id)
																															engine.say(my_message)
																													  
																															engine.runAndWait()

																															messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")


																											speak("you have entered wrong log-in creditionals")
	 
			y=Button(mn,fg='gray10',bg='yellow',bd=7,text="LOG IN",width=32,relief='raise',command=wa)
	 
			y.place(x=10,y=70)
	 
			mn.mainloop()
	 
		def vuser():
	 
			mn=Tk()
	 
			mn.config(bg='gray10')
	 
			mn.iconbitmap(r"hms.ico")
	 
			mn.title("LOG IN USER")
	 
			mn.geometry("255x110")
	 
			mn.resizable(0,0)
	 
			name=StringVar()
	 
			passc=StringVar()
	 
			e=Label(mn,bg='gray10',fg='cyan',text="Enter User Name :")
	 
			e.place(x=10,y=10)
	 

			q=ttk.Entry(mn,textvariable=name)
	 
			q.place(x=120,y=10)
	 
			p=Label(mn,bg='gray10',fg='cyan',text="Enter Password :")
 
			p.place(x=10,y=40)
 
			w=ttk.Entry(mn,textvariable=passc,show='*')
 
			w.place(x=120,y=40)
  
 
			def wu ():
 
				ussser=q.get()
 
				user=str(ussser)
 
				ppass=w.get()
 
				try :
 
					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')
 
					cur = conn.cursor()
 
					conn = cx_Oracle.connect(f'system/{orname.get()}@localhost')
 
					cur = conn.cursor()
 
					xm = cur.execute("select  username from UNLOCK_FOR_USER where pass = '%s' "%ppass)
 
					for i in xm:
 
						pr2=i
 
					if pr2 == (ussser,) :
 
						mn.destroy()         
 
						fu()
 
					else:

						def speak(my_message):

							engine = pyttsx3.init()

							rate = engine.getProperty('rate')
							voices_in_our_pc=engine.getProperty('voices')
							engine.setProperty('rate',150)
							engine.setProperty('voice',voices_in_our_pc[1].id)
							engine.say(my_message)
						  
							engine.runAndWait()

							messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")


						speak("you have entered wrong log-in creditionals")
						
				except:

																											def speak(my_message):

																															engine = pyttsx3.init()

																															rate = engine.getProperty('rate')
																															voices_in_our_pc=engine.getProperty('voices')
																															engine.setProperty('rate',150)
																															engine.setProperty('voice',voices_in_our_pc[1].id)
																															engine.say(my_message)
																													  
																															engine.runAndWait()

																															messagebox.showinfo("LOG IN DENIED","Please enter correct log in details")


																											speak("you have entered wrong log-in creditionals")
 
			y=Button(mn,fg='gray10',bg='cyan',bd = 7,relief='raise',text="LOG  IN",width=32,command=wu)
 
			y.place(x=10,y=70)
 
			mn.mainloop()


		def say2(my_message):
			
			engine = pyttsx3.init()

			rate = engine.getProperty('rate')
			
			voice=engine.getProperty('voices')
			
			engine.setProperty('rate',150)
			
			engine.setProperty('voice',voice[0].id)
			
			engine.say(my_message)

			engine.runAndWait()
			
			r = Tk()
 
			r.iconbitmap(r"hms.ico")
	
			r.title("Verification")
	
			r.resizable(0, 0)
	
			m = Frame(r)
	
			m.pack()
	
			c = Canvas(m, width=650, height=430)
	
			c.pack()
	
			p = PhotoImage(file=r"hms3.png")
	
			c.create_image(0, 0, image=p, anchor="nw")
	
			l = Label(m, text="Hospital Mangement System", font=('castellar', 16, 'bold', 'italic'),bg= 'light gray', fg="black")
	
			l.place(x=120, y=10)
	
			value = IntVar()
	
			value.set(2)
	
			photo = PhotoImage(file=r"hms2.png")
	
			photo0 = PhotoImage(file=r"hms1.png")

			def vvadmin():
															r.destroy()

															vadmin()
										
			rd0 = Radiobutton(m, image=photo, bg="light gray", value=1, variable=value, command=vvadmin)
	
			rd0.place(x=65, y=70)
	
			lb0 = Label(m, text="Administrator", font=('castellar', 30, 'bold', 'italic'), height=2)
	
			lb0.place(x=219, y=70)

			def vvuser():

														 r.destroy()

														 vuser()

															
	
			rd = Radiobutton(m, image=photo0, bg="light gray", value=2, variable=value, command=vvuser)
	
			rd.place(x=65, y=200)
	
			lb = Label(m, text="user", font=('castellar', 30, 'bold', 'italic'), height=2)
	
			lb.place(x=200, y=200)
	
			x = value.get()
	
			def bg5():
	
				p.config(file=r"hms3.png")
	
				btn0.config(command=bg)
	
			def bg4():
	
				p.config(file=r"hms4.png")
	
				btn0.config(command=bg5)
	
			def bg3():
	
				p.config(file=r"hms5.png")
	
				btn0.config(command=bg4)
	
			def  bg2():
	
				p.config(file=r"hms6.png")
	
				btn0.config(command=bg3)
	
			def bg1():
	
				p.config(file=r"hms7.png")
	
				btn0.config(command=bg2)
	
			def bg0():
	
				p.config(file=r"hms8.png")
	
				btn0.config(command=bg1)
	
			def bg():
	
				p.config(file=r"hms9.png")
	
				btn0.config(command=bg0)

			def exitt():

				def say1(my_message):
				
					engine1 = pyttsx3.init()

					rate1 = engine1.getProperty('rate')
					
					voice1=engine1.getProperty('voices')
					
					engine1.setProperty('rate',150)
					
					engine1.setProperty('voice',voice[0].id)
					
					engine1.say(my_message)
					
					engine1.runAndWait()

					f=messagebox.askokcancel("Verification","Confirm if you wan to exit")
	 
					if f > 0:
		
						r.destroy()
				

				message1='''

				Do You want to exit 
				'''

				say1(message1)
 
			btn = Button(m, text="EXIT", font=("algerian", 20, "bold"), bg="gray", height=1, width=30, bd=7,relief = 'raise',command=exitt)
	
			btn.place(x=45, y=320)
	
			phot = PhotoImage(file=r"hms0.png")
	
			btn0 = Button(m, image = phot,command=bg,bg='black')
	
			btn0['border']='0'
	
			btn0.place(x=0, y=0)
			
			r.mainloop()


		message2='''

		Hello 
		Welcome to my hospital management system
		this project is made by Vaibhav Gaur

		Now


		lets get started 

		Choose whether you are administrator or user
		'''

		say2(message2)
 
	r = Tk()
 
	r.iconbitmap(r"hms.ico")
 
	r.resizable(0, 0)
 
	r.title("HOSPITAL MANGEMENT SYSTEM")
 
	a=ttk.Progressbar(r,style='TProgressbar',orient='horizontal',length=1000,mode='determinate')
 
	a.pack()
 
	status = Label(r, text="Click button to start process..",bg='light gray', relief=SUNKEN, anchor=W, bd=2)
 
	status.pack(side=BOTTOM, fill=X)
 
	a.start()
 
	status.config(text='Working on it ........')
 
	a['maximum']=1000
 
	for i in range(1001):
 
		a['value']=i
 
		a.update()
 
	a['value']=0
 
	a.stop()
 
	r.destroy()
 
	main()

r= Tk()

r.iconbitmap(r"hms.ico")

r.title('Oracle Database')

r.resizable(0,0)

r.wm_attributes("-alpha",0.8)

orname = StringVar()

lb = ttk.Label(r , text = 'Please enter the password of your oracle database :-' ,font=('arial',12,'bold'))

lb.pack()

ent = Entry(r , fg='dark gray', width =27 , show = '@' , font=('arial',20,'bold') , textvariable = orname)

ent.pack()

ent.focus_set()


def okk():

	if ent.get() == '' :

		def say3(my_message):
			
			engine = pyttsx3.init()

			rate = engine.getProperty('rate')
			
			voice=engine.getProperty('voices')
			
			engine.setProperty('rate',150)
			
			engine.setProperty('voice',voice[0].id)
			
			engine.say(my_message)
			
			engine.runAndWait()

			messagebox.showinfo("Oracle Database","Please do not leave it blank")
			

		message3='''

		You have left the entry field blank

		Please do not leave it blank
		'''

		say3(message3)

	else:    

		try:

			cx_Oracle.connect(f'system/{orname.get()}@localhost')

			r.destroy()

			main0()

		except:

			def say4(my_message):
			
				engine = pyttsx3.init()

				rate = engine.getProperty('rate')
				
				voice=engine.getProperty('voices')
				
				engine.setProperty('rate',150)
				
				engine.setProperty('voice',voice[0].id)
				
				engine.say(my_message)
				
				engine.runAndWait()

				messagebox.showinfo("Oracle Database","Please enter correct password")

			message4='''

			You have entered wrong database password
			'''

			say4(message4)

def leave():

	def say5(my_message):
	
		engine = pyttsx3.init()

		rate = engine.getProperty('rate')
		
		voice=engine.getProperty('voices')
		
		engine.setProperty('rate',150)
		
		engine.setProperty('voice',voice[0].id)
		
		engine.say(my_message)
		
		engine.runAndWait()

		f=messagebox.askokcancel("Verification","Confirm if you wan to exit")

		if f > 0:

			r.destroy()
	

	message5='''

	Do You want to exit 
	'''

	say5(message5)        

btn = ttk.Button(r,text = ' NEXT >> ',command = okk , width=33)

btn.pack(side=LEFT)

btn0 = ttk.Button(r,text = ' CANCEL ',command = leave, width=33)

btn0.pack(side=RIGHT)

r.mainloop()                    
