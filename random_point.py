import turtle
import random
screen = turtle.Screen()
for i in range(5):
    ranX = random.randrange(-100, 100)
    ranY = random.randrange(-100, 100)
    turtle.Turtle().goto(ranX, ranY)

screen.mainloop()
