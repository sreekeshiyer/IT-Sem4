from tkinter import *
root = Tk()
var1 = IntVar()
c1_button = Checkbutton(root, text='Music', variable=var1)
temp = IntVar()
c2_button = Checkbutton(root, text='Video', variable=temp)
c1_button.pack()
c2_button.pack()
mainloop()
