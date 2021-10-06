from tkinter import *
master = Tk()
w = Scale(master, from_=0, to=20)
w.pack()
w = Scale(master, from_=0, to=100, orient=HORIZONTAL)
w.pack()
mainloop()
