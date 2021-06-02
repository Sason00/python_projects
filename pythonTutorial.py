import turtle

screen = turtle.Screen()
batz = turtle.Turtle()
batz.pendown()
batz.pensize(5)
batz.shape("turtle")

color = "red"
e = 1
for i in range(50):
    if color == "red":
        batz.pencolor(color)
        color = "blue"
        
    elif color == "blue":
        batz.pencolor(color)
        color = "red"

    batz.forward(150)
    batz.left(90)
    i = i + 1
    if i == 4:
        batz.left(30)

    elif i == 8:
        batz.left(30)

    elif i == 12:
        batz.left(30)

    elif i == 16:
        batz.left(30)

    elif i == 20:
        batz.left(30)

    elif i == 24:
        batz.left(30)

    elif i == 28:
        batz.left(30)

    elif i == 32:
        batz.left(30)

    elif i == 36:
        batz.left(30)

    elif i == 40:
        batz.left(30)

    elif i == 44:
        batz.left(30)

batz.penup()
batz.goto(400, 0)
color = "green"
for d in range(12):
    if color == "green":
        batz.pencolor(color)
        color = "black"

    elif color == "black":
        batz.pencolor(color)
        color = "green"
        
    batz.pendown()
    batz.pensize(5)
    batz.circle(35)
    batz.left(30)

screen.exitonclick()
