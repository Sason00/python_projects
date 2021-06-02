import turtle

def fillRect(x, y, width, height, color = "#000000"):
    rect = turtle.Turtle()
    rect.penup()
    rect.color(color)
    rect.begin_fill()
    rect.speed(9999)
    rect.setpos(x, y)
    rect.pendown()
    rect.forward(width)
    rect.right(90)
    rect.forward(height)
    rect.left(90)
    rect.forward(-width)
    rect.right(90)
    rect.forward(-height)
    rect.end_fill()
    
def fillStroke(x, y, width, height, color = "#000000"):
    rect = turtle.Turtle()
    rect.penup()
    rect.color(color)
    rect.speed(9999)
    rect.setpos(x, y)
    rect.pendown()
    rect.forward(width)
    rect.right(90)
    rect.forward(height)
    rect.left(90)
    rect.forward(-width)
    rect.right(90)
    rect.forward(-height)

def clearRect(x, y, width, height):
    clear = turtle.Turtle()
    clear.penup()
    clear.color("#000000")
    clear.speed(9999)
    clear.setpos(x, y)
    clear.pendown()
    clear.begin_fill()
    clear.forward(width)
    clear.right(90)
    clear.forward(height)
    clear.left(90)
    clear.forward(-width)
    clear.right(90)
    clear.forward(-height)
    clear.end_fill()


screen = turtle.Screen()
fillRect(100, 100, 50, 50, "red")
screen.mainloop()