from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir='D:\\microverse\\python\\python-lesson',
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file",".txt"),
                                        ("HTML",".html"),
                                        ("All files",".*")
                                    ])
    if file is None:
        return
    # fileText = str(text.get(1.0,END))
    fileText = input("Enter some text: ")
    file.write(fileText)
    file.close()

window = Tk()
button = Button(text='save',
                command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()