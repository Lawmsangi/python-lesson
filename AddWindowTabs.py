from tkinter import *
from tkinter import ttk

window = Tk()

notebook = ttk.Notebook(window)   #widget that manages a collection of windows/displays

tab1 = Frame(notebook)  #new frame for tab1
tab2 = Frame(notebook)

notebook.add(tab1,text="Tab1")
notebook.add(tab2,text="Tab2")
notebook.pack(expand=True,fill="both")  #expand to fill any spaces not otherwise used
                                        #fill = fill space on x and y axis
Label(tab1,text="Hello this is tab1",height=25,width=50).pack()
Label(tab2,text="Goodbye this is tab2",height=25,width=50).pack()

window.mainloop()