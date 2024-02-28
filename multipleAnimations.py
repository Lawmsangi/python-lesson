from tkinter import *
import time
from Ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"yellow")
cricket_ball = Ball(canvas,0,0,70,3,2,"green")

while True:
    volley_ball.move()
    tennis_ball.move()
    cricket_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()