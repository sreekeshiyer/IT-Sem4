from tkinter import *
main = Tk()
ourMessage ='Your transaction was a success!'
messageVar = Message(main, text = ourMessage)
messageVar.config(bg='lightgreen')
messageVar.pack( )
main.mainloop( )