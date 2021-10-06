from tkinter import * 


def click(event):
	get = event.widget.cget("text")
	
	if get == "C":
		val.set("")
		e.update()

	elif get == "=":
		if val.get().isdigit():
			value = int(val.get())
		else:
			try:
				value = eval(e.get())

			except:
				value = "Error"

			
		val.set(value)
		e.update()

	else:
		val.set(val.get()+get)
	e.update()



root = Tk()

root.geometry("300x420")
root.maxsize(300, 420)
root.title("My_Calculator")
root.iconphoto(False, PhotoImage(file='s2.png'))


val = StringVar()
e = Entry(root, textvariable=val, font=(None,30,"bold"))
e.pack(fill=X, padx=6, pady=4)



l1 = [7,8,9,"C"]
l2 = [4,5,6,"/"]
l3 = [1,2,3,"-"]
l4 = [0,"*","+","="]


f = Frame(root, borderwidth=4, bg="grey")
for i in l1:
	b = Button(f, text=f"{i}",font=(None,24,"bold"),borderwidth=5)
	b.pack(side=LEFT, padx=8, pady=2)
	b.bind("<Button>", click)
f.pack(fill=X, padx=7, pady=4)

f = Frame(root, borderwidth=4, bg="grey")
for i in l2:
	b = Button(f, text=f"{i}",font=(None,24,"bold"),borderwidth=5)
	b.pack(side=LEFT, padx=8, pady=2)
	b.bind("<Button>", click)
f.pack(fill=X, padx=7, pady=4)

f = Frame(root, borderwidth=4, bg="grey")
for i in l3:
	b = Button(f, text=f"{i}",font=(None,24,"bold"),borderwidth=5)
	b.pack(side=LEFT, padx=8, pady=2)
	b.bind("<Button>", click)
f.pack(fill=X, padx=7, pady=4)

f = Frame(root, borderwidth=4, bg="grey")
for i in l4:
	b = Button(f, text=f"{i}",font=(None,24,"bold"),borderwidth=5)
	b.pack(side=LEFT, padx=8, pady=2)
	b.bind("<Button>", click)
f.pack(fill=X, padx=7, pady=4)



root.configure(background="black")
root.mainloop()