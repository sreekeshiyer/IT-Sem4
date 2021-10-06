from tkinter.ttk import *
from tkinter import *
import mysql.connector
from tkinter import messagebox


mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)

mycursor=mydb.cursor()
root=Tk()
root.title("Student Data")
root.geometry("440x410")

label1 = Label(root, text="Roll No.", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=1, column=0, padx=(10,0))
label2 = Label(root, text="First Name", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=2, column=0, padx=(10,0))
label3 = Label(root, text="Last Name", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=3, column=0, padx=(10,0))
label4 = Label(root, text="Phone Number", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=4, column=0, padx=(10,0))
label5 = Label(root, text="City", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=5, column=0, padx=(10,0))
label6 = Label(root, text="State", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=6, column=0, padx=(10,0))
label7 = Label(root, text="Age", width=13, anchor='w', font=("Sylfaen", 12)).grid(row=7, column=0, padx=(10,0))

e1 = Entry(root, width=30)
e1.grid(row=1, column=1, padx=(0,20), pady = 20)
e2 = Entry(root, width=30)
e2.grid(row=2, column=1, padx=(0,20), pady = 20)
e3 = Entry(root, width=30)
e3.grid(row=3, column=1, padx=(0,20), pady = 20)
e4 = Entry(root, width=30)
e4.grid(row=4, column=1, padx=(0,20), pady = 20)
e5 = Entry(root, width=30)
e5.grid(row=5, column=1, padx=(0,20), pady = 20)
e6 = Entry(root, width=30)
e6.grid(row=6, column=1, padx=(0,20), pady = 20)
e7 = Entry(root, width=30)
e7.grid(row=7, column=1, padx=(0,20), pady = 20)

def Register():
    RollNo=int(e1.get())
    dbRollNo=""
    Select="select RollNo from student where RollNo=%s" %(RollNo)
    mycursor.execute(Select)
    result=mycursor.fetchall()
    for i in result:
        dbRollNo=i[0]
    if(RollNo == dbRollNo):
        messagebox.askokcancel("Information","Record Already exists")
    else:
        Insert="Insert into student(RollNo,First_Name,Last_Name,Phone_Number,City,State,Age) values(%s,%s,%s,%s,%s,%s,%s)"
        First_Name=e2.get()
        Last_Name=e3.get()
        Phone_Number=e4.get()
        City=e5.get()
        State=e6.get()
        Age=e7.get()
        if(First_Name !="" and Last_Name !="" and Phone_Number !="" and City !="" and State !="" and Age !=""):
            Value=(RollNo,First_Name,Last_Name,Phone_Number,City,State,Age)
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
            if (First_Name == "" and Last_Name == "" and Phone_Number == "" and City == "" and State == "" and Age == ""):
             messagebox.askokcancel("Information","New Entery Fill All Details")
            else:
             messagebox.askokcancel("Information", "Some fields left blank")

def ShowRecord():
    RollNo=int(e1.get())
    dbRollNo=""
    Select="select RollNo from student where RollNo=%s" %(RollNo)
    mycursor.execute(Select)
    result1=mycursor.fetchall()
    for i in result1:
        dbRollNo=i[0]
    Select1="select First_Name,Last_Name,Phone_Number,City,State,Age from student where RollNo='%s'" %(RollNo)
    mycursor.execute(Select1)
    result2=mycursor.fetchall()
    First_Name=""
    Last_Name=""
    Phone_Number=""
    City=""
    State=""
    Age=""
    if(RollNo == dbRollNo):
        for i in result2:
            First_Name=i[0]
            Last_Name=i[1]
            Phone_Number=i[2]
            City=i[3]
            State=i[4]
            Age=i[5]
        e2.insert(0,First_Name)
        e3.insert(0, Last_Name)
        e4.insert(0, Phone_Number)
        e5.insert(0, City)
        e6.insert(0, State)
        e7.insert(0, Age)
    else:
        messagebox.askokcancel("Information","No Record exists")

def Delete():
    RollNo=int(e1.get())
    Delete="delete from student where RollNo=%s" %(RollNo)
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
    RollNo=int(e1.get())
    First_Name=e2.get()
    Last_Name=e3.get()
    Phone_Number=e4.get()
    City=e5.get()
    State=e6.get()
    Age=e7.get()
    Update="Update student set First_Name='%s', Last_Name='%s', Phone_Number='%s', City='%s', State='%s', Age='%s' where RollNo='%s'" %(First_Name,Last_Name,Phone_Number,City,State,Age,RollNo)
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
            tv.heading('5', text='City')
            tv.heading('6', text='State')
            tv.heading('7', text='Age')
            
            tv.grid(sticky=(N,S,W,E))
            self.tview = tv
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

        def LoadTable(self):
            Select="Select * from student"
            mycursor.execute(Select)
            result=mycursor.fetchall()
            RollNo=""
            First_Name=""
            Last_Name=""
            Phone_Number=""
            City=""
            State=""
            Age=""
            for i in result:
                RollNo=i[0]
                First_Name=i[1]
                Last_Name=i[2]
                Phone_Number=i[3]
                City=i[4]
                State=i[5]
                Age=i[6]
                self.tview.insert("",'end',text="L1",values=(RollNo,First_Name,Last_Name,Phone_Number,City,State,Age))
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

button1 = Button(root, text="Register", width=10, bg="LightSkyBlue1", command=Register)
button1.grid(row=1,column=3)
button2 = Button(root, text="Delete", width=10, bg="LightSkyBlue2", command=Delete)
button2.grid(row=2,column=3)
button3 = Button(root, text="Update", width=10, bg="LightSkyBlue3", command=Update)
button3.grid(row=3,column=3)
button4 = Button(root, text="Show record", width=10, bg="SkyBlue1", command=ShowRecord)
button4.grid(row=4,column=3)
button5 = Button(root, text="Show All", width=10, bg="SkyBlue2", command=Showall)
button5.grid(row=5,column=3)
button6 = Button(root, text="Clear", width=10, bg="SkyBlue3", command=Clear)
button6.grid(row=6,column=3)

root.mainloop()