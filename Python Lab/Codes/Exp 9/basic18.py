import tkinter
import tkinter.messagebox

top = tkinter.Tk()
def hello():
   tkinter.messagebox.showinfo("Say Hello", "Hello World")

B1 = tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()