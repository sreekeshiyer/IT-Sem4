from tkinter import *
def onclick():
   pass
root = Tk()
text = Text(root)
text.insert(INSERT, "Hello, There.....")
text.insert(END, "\n\nGeneral Kenobi.....")
text.pack()
text.tag_add("here", "1.0", "1.8")
text.tag_add("start", "1.13", "1.16")
text.tag_config("here", background="#2ff2fF", foreground="blue")
text.tag_config("start", background="black", foreground="white")
root.mainloop()
