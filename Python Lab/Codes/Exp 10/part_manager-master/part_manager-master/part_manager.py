from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS user (user_id INTEGER PRIMARY KEY, fname text, lname text, city text, gender text, age INTEGER)")
        self.conn.commit()
    def fetch(self):
        self.cur.execute("SELECT * FROM user")
        rows = self.cur.fetchall()
        return rows
    def insert(self, user_id, fname, lname, city, gender, age):
        self.cur.execute("INSERT INTO user VALUES (?, ?, ?, ?, ?, ?)",
                         (user_id, fname, lname, city, gender, age))
        self.conn.commit()
    def remove(self, user_id):
        self.cur.execute("DELETE FROM user WHERE user_id=?", (user_id,))
        self.conn.commit()
    def update(self, user_id, fname, lname, city, gender, age):
        self.cur.execute("UPDATE user SET fname = ?, lname = ?, city = ?, gender = ?, age = ? WHERE user_id = ?",
                         (fname, lname, city, gender, age, user_id))
        self.conn.commit()
    def __del__(self):
        self.conn.close()

def add_item():
    if rollVar.get() == '' or fnameVar.get() == '' or lnameVar.get() == '' or cityVar.get() == '' or genderVar.get() == '' or ageVar.get() == 0:
        messagebox.showerror('Required Fields', 'Please include all fields')
        return
    db.insert(rollVar.get(), fnameVar.get(),lnameVar.get(),cityVar.get(),genderVar.get(), ageVar.get())
    listbox.delete(0, END)
    listbox.insert(END, (rollVar.get(), fnameVar.get(),lnameVar.get(),cityVar.get(),genderVar.get(), ageVar.get()))
    clear_text()
    listbox.delete(0, END)
    for row in db.fetch():
        listbox.insert(END, row)

def select_item(event):
    try:
        global selected_item
        index = listbox.curselection()[0]
        selected_item = listbox.get(index)
        rollVar.set(selected_item[0])
        fnameVar.set(selected_item[1])
        lnameVar.set(selected_item[2])
        cityVar.set(selected_item[3])
        genderVar.set(selected_item[4])
        ageVar.set(selected_item[5])
    except IndexError:
        pass

def remove_item():
    db.remove(selected_item[0])
    clear_text()
    listbox.delete(0, END)
    for row in db.fetch():
        listbox.insert(END, row)

def update_item():
    db.update(selected_item[0], fnameVar.get(),lnameVar.get(),cityVar.get(),genderVar.get(), ageVar.get())
    listbox.delete(0, END)
    for row in db.fetch():
        listbox.insert(END, row)

def clear_text():
    rollEntry.delete(0, END)
    fnameEntry.delete(0, END)
    lnameEntry.delete(0, END)
    cityMenu.delete(0, END)
    ageSpinbox.delete(0,END)

db = Database('store.db')

app = Tk()
app.configure(bg='light cyan')
app.title('CRUD Application')
app.geometry('446x500')

rollVar = IntVar()
rollLabel = Label(app ,text = "User ID",bg="light cyan",width=30, anchor='w').grid(row = 0,column = 0)
rollEntry = Entry(app,textvariable=rollVar)
rollEntry.grid(row = 0,column = 1,pady=10)

fnameVar = StringVar()
fnameLabel = Label(app ,text = "First Name",bg="light cyan",width=30, anchor='w').grid(row = 1,column = 0)
fnameEntry = Entry(app,textvariable=fnameVar)
fnameEntry.grid(row = 1,column = 1,pady=10)

lnameVar = StringVar()
lnameLabel = Label(app ,text = "Last Name",width=30, anchor='w',bg="light cyan").grid(row = 2,column = 0)
lnameEntry = Entry(app,textvariable=lnameVar)
lnameEntry.grid(row = 2,column = 1,pady=10)

cityVar = StringVar()
cityLabel = Label(app ,text = "Select City",width=30, anchor='w',bg="light cyan").grid(row = 3,column = 0)
cityMenu = ttk.Combobox(app,width=17,textvariable=cityVar)
cityMenu['values']=('Mumbai','Chennai','Delhi','Thrissur','Kochi','Palakkad','Mangalore','Rajkot','Surat')
cityMenu.grid(row = 3,column = 1,pady=10)

genderLabel = Label(app ,text = "Gender",width=30, anchor='w',bg="light cyan").grid(row = 4,column = 0)
frame = Frame(app,bg="light cyan")
frame.grid(row=4,column=1,pady=10)
genderVar = StringVar()
dr1=Radiobutton(frame,text='Male',variable = genderVar,value='Male', tristatevalue="x",bg="light cyan")
dr1.pack(side=LEFT)
dr2=Radiobutton(frame,text='Female',variable = genderVar,value='Female', tristatevalue="x",bg="light cyan")
dr2.pack(side=LEFT)

ageVar = IntVar()
ageLabel = Label(app ,text = "Age",width=30, anchor='w',bg="light cyan").grid(row = 5,column = 0)
ageSpinbox = Spinbox(app, from_=1, to=130, width=19,textvariable=ageVar)
ageSpinbox.grid(row=5,column=1,pady=10)

listbox = Listbox(app, height=11, width=70)
listbox.grid(row=7, column=0, columnspan=3, rowspan=6, padx=10)
listbox.bind('<<ListboxSelect>>', select_item)

frame1 = Frame(app, bg="light cyan")
frame1.grid(row=6,column=0,columnspan=4,pady=20)
add_btn = Button(frame1, text='Insert', width=12, command=add_item)
add_btn.pack(side=LEFT)
remove_btn = Button(frame1, text='Delete', width=12, command=remove_item)
remove_btn.pack(side=LEFT)
update_btn = Button(frame1, text='Update', width=12, command=update_item)
update_btn.pack(side=LEFT)
clear_btn = Button(frame1, text='Clear Input', width=12, command=clear_text)
clear_btn.pack(side=LEFT)

listbox.delete(0, END)
for row in db.fetch():
    listbox.insert(END, row)

app.mainloop()