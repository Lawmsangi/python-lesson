from tkinter import *

def display():
    if(x.get()):
        print("You agree")
    else:
        print("You don't agree :(")

window = Tk()
x = BooleanVar()
python_img = PhotoImage(file='python_img.png')
check_button = Checkbutton(window,
                           text="I agree to something",
                           variable=x,
                           onvalue=True,
                           offvalue=False,
                           command=display,
                           font=("Arial",20),
                           fg="#00ff00",
                           bg="black",
                           activebackground="black",
                           activeforeground="#00ff00",
                           padx=25,
                           pady=10,
                           image=python_img,
                           compound='left'
                           )
check_button.pack()
window.mainloop()