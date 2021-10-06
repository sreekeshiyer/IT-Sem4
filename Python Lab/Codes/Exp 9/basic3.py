from tkinter import *
master = Tk()
var1 = IntVar()
c1 = Checkbutton(master, text='Music', variable=var1)
var2 = IntVar()
c2 = Checkbutton(master, text='Video', variable=var2)
c1.pack()
c2.pack()
mainloop()