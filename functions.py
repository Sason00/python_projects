import turtle
import math

screen = turtle.Screen()
screen.setup(500, 500)

m = input("put here your m value: ")
operator1 = input("put here your first operator: ")
b = input("put here your b value: ")
operator2 = input("put here your second operator: ")

fun1 = m + operator1
fun2 = operator2 + b

x_line = turtle.Turtle()
x_line.speed(0)
x_line.hideturtle()
x_line.penup()
x_line.goto(0, -250)
x_line.pendown()
x_line.goto(0, 250)

y_line = turtle.Turtle()
y_line.speed(0)
y_line.hideturtle()
y_line.penup()
y_line.goto(-250, 0)
y_line.pendown()
y_line.goto(250, 0)

function = turtle.Turtle()
function.penup()
function.goto(-250, -250)
function.speed(0)
function.hideturtle()

for i in range(-250, 250):
    try:
        x = str(i)
        y = eval(fun1 + "" + x + "" + fun2)
        print(x, y)
        function.goto(int(x), int(y))
        function.pendown()
        # if y > 250:
        #    break
    except:
        pass

screen.mainloop()
