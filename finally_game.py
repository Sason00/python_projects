import turtle
import random

player_choise = input()
print("you chose: " + player_choise)

screen = turtle.Screen()

blue_step = 0
red_step = 0
green_step = 0

blue_turtle = turtle.Turtle()
blue_turtle.penup()
blue_turtle.color("blue")
blue_turtle.setpos(0, 0)
blue_turtle.left(90)
def blue():
    blue_turtle.forward(blue_step)
    if blue_step >= 100:
        print(blue_mes)
        global red_mes
        global green_mes
        red_mes = " "
        green_mes = " "
        if player_choise == "blue":
            print("you won!!!")
        else:
            print("you lost")
    
red_turtle = turtle.Turtle()
red_turtle.penup()
red_turtle.color("red")
red_turtle.setpos(15, 0)
red_turtle.left(90)
def red():
    red_turtle.forward(red_step)
    if red_step >= 100:
        print(red_mes)
        global blue_mes
        global green_mes
        blue_mes = " "
        green_mes = " "
        if player_choise == "red":
            print("you won!!!")
        else:
            print("you lost")
    
green_turtle = turtle.Turtle()
green_turtle.penup()
green_turtle.color("green")
green_turtle.setpos(30, 0)
green_turtle.left(90)
def green():
    green_turtle.forward(green_step)
    if green_step >= 100:
        print(green_mes)
        global red_mes
        global blue_mes
        red_mes = " "
        blue_mes = " "
        if player_choise == "green":
            print("you won!!!")
        else:
            print("you lost")
    
blue_turtle_speed = random.randrange(1, 7)
red_turtle_speed = random.randrange(1, 7)
green_turtle_speed = random.randrange(1, 7)

blue_mes = "blue won"
red_mes = "red won"
green_mes = "green won"

while True:
    blue_step += blue_turtle_speed
    red_step += red_turtle_speed
    green_step += green_turtle_speed

    blue()
    red()
    green()

screen.mainloop()


