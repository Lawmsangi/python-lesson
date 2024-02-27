from tkinter import *
from tkinter import messagebox  #import messagebox library

def click():
    # messagebox.showinfo(title='This is an info message box',
    #                     message='You are a person')

    # messagebox.showwarning(title="WARNING!",
    #                        message="You have a VIRUS!!")
    # messagebox.showerror(title="ERROR!!",message="Something went wrong!")
    # if messagebox.askokcancel(title='ask ok cancel',message='do you want to do the thing?'):
    #     print("You did a thing")
    # else:
    #     print("you cancel a thing")

    # if messagebox.askretrycancel(title='ask retry cancel',message='you want to retry?'):
    #     print("You Retry!")
    # else:
    #     print("you cancel")

    # if messagebox.askyesno(title='Ask yes or no',message="do you like cake?"):
    #     print("I like cake too")
    # else:
    #     print("Why do you not like cake?")

    # answer = messagebox.askquestion(title='ask questions',message='do you like pie')
    # if answer == 'yes':
    #     print("I like pie too")
    # else:
    #     print("why do you not like pie")
    answer = messagebox.askyesnocancel(title='yes no cancel',
                                       message='do you like to code',
                                       icon='info'
                                       )
    if (answer == True):
        print("you like to code :)")
    elif (answer == False):
        print("why are you looking to my repo?")
    else:
        print('you have dodged the question')
window = Tk()

button = Button(window,command=click,text='click me')
button.pack()

window.mainloop()