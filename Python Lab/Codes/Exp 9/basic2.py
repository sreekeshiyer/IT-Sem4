import tkinter as tk
r = tk.Tk()
r.title('Hello')
button = tk.Button(r, text='Click me to close window!', width=25, height=5, command=r.destroy)
button.pack()
r.mainloop()