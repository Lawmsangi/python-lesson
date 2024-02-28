from tkinter import *

def doSomething(event):
    # print("You presses: "+ event.keysym)
    label.config(text=event.keysym)

window = Tk()

window.bind("<Key>",doSomething)

label = Label(window,font=("Helvetica",50))
label.pack()

window.mainloop()