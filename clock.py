import turtle
import time

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.tracer(0)

clock = turtle.Turtle()
clock.shape("circle")
clock.shapesize(25)
clock.color("white")
hour_pen = turtle.Turtle()
hour_pen.setheading(90)
hour_pen.shape("arrow")
hour_pen.shapesize(stretch_wid=0.2, stretch_len=10)
minute_pen = turtle.Turtle()
minute_pen.setheading(90)
minute_pen.color("red")
minute_pen.shape("arrow")
minute_pen.shapesize(stretch_wid=0.2, stretch_len=18)
second_pen = turtle.Turtle()
second_pen.setheading(90)
second_pen.color("blue")
second_pen.shape("arrow")
second_pen.shapesize(stretch_wid=0.2, stretch_len=20)

# to turn one hour hour_pen.right(30) minute hour_pen.right(6) and seconds to
# to get time time.strftime("%H,%M,%S")

while True:
    if int(time.strftime("%H")) >= 12:
        hour_pen.setheading((int(time.strftime("%H")) - 12) * -30 - 90)
    else:
        hour_pen.setheading(int(time.strftime("%H")) * -30 - 90)
    minute_pen.setheading(int(time.strftime("%M")) * -6 - 90)
    second_pen.setheading(-1 * int(time.strftime("%S")) * 6 - 90)
    screen.update()
    screen.tracer(1)
    time.sleep(0.01)

# screen.mainloop()
