from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_class"
)

mycursor=mydb.cursor()
root=Tk()
root.title("Student Details")
root.geometry("850x400")
root.configure(background="lavender")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")

label1 = Label(root, text="Roll No.", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))
label2 = Label(root, text="First Name", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=4, padx=(10,0))
label3 = Label(root, text="Last Name", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
label4 = Label(root, text="Phone Number", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=4, padx=(10,0))
label5 = Label(root, text="city", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
label6 = Label(root, text="state", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=4, padx=(10,0))
label7 = Label(root, text="age", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=2, padx=(10,0))

e1 = Entry(root, width=20)
e1.grid(row=1, column=1, padx=(0,10), pady = 20)
e2 = Entry(root, width=20)
e2.grid(row=1, column=5, padx=(0,10), pady = 20)
e3 = Entry(root, width=20)
e3.grid(row=2, column=1, padx=(0,10), pady = 20)
e4 = Entry(root, width=20)
e4.grid(row=2, column=5, padx=(0,10), pady = 20)
e5 = Entry(root, width=20)
e5.grid(row=3, column=1, padx=(0,10), pady = 20)
e6 = Entry(root, width=20)
e6.grid(row=3, column=5, padx=(0,10), pady = 20)
e7 = Entry(root, width=20)
e7.grid(row=4, column=3, padx=(0,10), pady = 20)

def Register():
    roll_no=e1.get()
    dbroll_no=""
    Select="select roll_no from student where roll_no='%s'" %(roll_no)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbroll_no=i[0]
    if(roll_no == dbroll_no):
        messagebox.askokcancel("Information","Record Already exists")
    else:
        Insert="Insert into student(roll_no,f_name,l_name,phone_number,city,state,age) values(%s,%s,%s,%s,%s,%s,%s)"
        f_name=e2.get()
        l_name=e3.get()
        phone_number=e4.get()
        city=e5.get()
        state=e6.get()
        age=e7.get()
        if(f_name !="" and l_name !="" and phone_number !="" and city !="" and state !="" and age !=""):
            Value=(roll_no,f_name,l_name,phone_number,city,state,age)
            mycursor.execute(Insert,Value)
            mydb.commit()
            messagebox.askokcancel("Information","Record inserted")
            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0, END)
            e6.delete(0, END)
            e7.delete(0, END)
        else:
            if (f_name == "" and l_name == "" and phone_number == "" and city == "" and state == "" and age == ""):
             messagebox.askokcancel("Information","New Entry Fill All Details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")

def ShowRecord():
    roll_no=e1.get()
    print(roll_no)
    dbroll_no=""
    Select="select roll_no from student where roll_no='%s'" %(roll_no)
    mycursor.execute(Select)
    result1=mycursor.fetchall()
    for i in result1:
        dbroll_no=i[0]
    Select1="select f_name,l_name,phone_number,city,state,age from student where roll_no='%s'" %(roll_no)
    mycursor.execute(Select1)
    result2=mycursor.fetchall()
    f_name=""
    l_name=""
    phone_number=""
    city=""
    state=""
    age=""
    if(str(roll_no) == str(dbroll_no)):
        for i in result2:
            f_name=i[0]
            l_name=i[1]
            phone_number=i[2]
            city=i[3]
            state=i[4]
            age=i[5]
        e2.insert(0,f_name)
        e3.insert(0, l_name)
        e4.insert(0, phone_number)
        e5.insert(0, city)
        e6.insert(0, state)
        e7.insert(0, age)
    else:
        messagebox.askokcancel("Information","No Record exists")

def Delete():
    roll_no=e1.get()
    Delete="delete from student where roll_no='%s'" %(roll_no)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information","Record Deleted")
    e1.delete(0,END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0,END)

def Update():
    roll_no=e1.get()
    f_name=e2.get()
    l_name=e3.get()
    phone_number=e4.get()
    city=e5.get()
    state=e6.get()
    age=e7.get()
    Update="Update student set f_name='%s', l_name='%s', phone_number='%s', city='%s', state='%s', age='%s' where roll_no='%s'" %(f_name,l_name,phone_number,city,state,age,roll_no)
    mycursor.execute(Update)
    mydb.commit()
    messagebox.showinfo("Info","Record Update")

def Showall():
    class A(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.CreateUI()
            self.LoadTable()
            self.grid(sticky=(N, S, W, E))
            parent.grid_rowconfigure(0, weight=1)
            parent.grid_columnconfigure(0, weight=1)

        def CreateUI(self):
            tv=Treeview(self)
            tv['columns']=('1', '2', '3', '4', '5', '6', '7')
            tv['show']='headings'

            tv.column("1", width = 90, anchor ='c')
            tv.column("2", width = 90, anchor ='c')
            tv.column("3", width = 90, anchor ='c')
            tv.column("4", width = 90, anchor ='c')
            tv.column("5", width = 90, anchor ='c')
            tv.column("6", width = 90, anchor ='c')
            tv.column("7", width = 90, anchor ='c')

            tv.heading('1', text='Roll No.')
            tv.heading('2', text='First Name')
            tv.heading('3', text='Last Name')
            tv.heading('4', text='Phone Number')
            tv.heading('5', text='city')
            tv.heading('6', text='state')
            tv.heading('7', text='age')
            
            tv.grid(sticky=(N,S,W,E))
            self.tview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def LoadTable(self):
            Select="Select * from student"
            mycursor.execute(Select)
            result=mycursor.fetchall()
            roll_no=""
            f_name=""
            l_name=""
            phone_number=""
            city=""
            state=""
            age=""
            for i in result:
                roll_no=i[0]
                f_name=i[1]
                l_name=i[2]
                phone_number=i[3]
                city=i[4]
                state=i[5]
                age=i[6]
                self.tview.insert("",'end',text="L1",values=(roll_no,f_name,l_name,phone_number,city,state,age))
    root=Tk()
    root.title("Overview Page")
    root.resizable(width = 1, height = 1)
    A(root)

def Clear():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)
    e5.delete(0, END)
    e6.delete(0, END)
    e7.delete(0, END)

button1 = Button(root, text="Register", width=10, bg="#06a099", command=Register,activebackground="skyblue2", activeforeground="white", background="skyblue2", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 11 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
button1.grid(row=8,column=0)
button2 = Button(root, text="Delete", width=10, bg="#06a099", command=Delete,activebackground="skyblue2", activeforeground="white", background="skyblue2", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 11 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
button2.grid(row=8,column=1)
button3 = Button(root, text="Update", width=10, bg="#06a099", command=Update,activebackground="skyblue2", activeforeground="white", background="skyblue2", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 11 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
button3.grid(row=8,column=2)
button4 = Button(root, text="Show record", width=10, bg="#06a099", command=ShowRecord,activebackground="skyblue2", activeforeground="white", background="skyblue2", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 11 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
button4.grid(row=8,column=3)
button5 = Button(root, text="Show All", width=10, bg="#06a099", command=Showall,activebackground="skyblue2", activeforeground="white", background="skyblue2", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 11 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
button5.grid(row=8,column=4)
button6 = Button(root, text="Clear", width=10, bg="#06a099", command=Clear,activebackground="skyblue2", activeforeground="white", background="skyblue2", disabledforeground="#a3a3a3", font="-family {Segoe UI Black} -size 11 -weight bold", foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black")
button6.grid(row=8,column=5)

root.mainloop()

