import tkinter as tk
root = tk.Tk()
root.title('With Button')
button=tk.Button(root, text='Click me to close window!', width=25, height=5, command=root.destroy)
button.pack()
root.mainloop()
