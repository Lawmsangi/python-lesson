from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir='D:\\microverse\\python\\python-lesson',
                                          title="Open file okay?",
                                          filetypes= (("filedialog files","*.txt"),
                                          ("all files","*.*")))
    file = open(filepath,'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(text="Open",
                command=openFile)
button.pack()
window.mainloop()