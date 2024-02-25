from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Lawmsangi's first GUI program")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#eee")
window.mainloop()