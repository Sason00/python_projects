import turtle
import tkinter as tk

screen = tk.Tk()
canvas = tk.Canvas(screen, width = 600, height = 500, cursor="plus").pack()

player1 = turtle.RawTurtle(canvas)
player1.penup()
player1.speed(-1)
player1.setx(-250)
player1.shape("square")

player2 = turtle.RawTurtle(canvas)
player2.penup()
player2.speed(-1)
player2.setx(250)
player2.shape("square")

ball = turtle.RawTurtle(canvas)
ball.penup()
ball.speed(-1)
ball.shape("square")
ball.color("red")
ball_mx = 3
ball_my = 3

def player1_up(x):
    player1.sety(player1.ycor() + 15)

def player1_down(x):
    player1.sety(player1.ycor() - 15)

def player2_up(x):
    player2.sety(player2.ycor() + 15)

def player2_down(x):
    player2.sety(player2.ycor() - 15)

screen.bind("w", player1_up)
screen.bind("s", player1_down)
screen.bind("<Up>", player2_up)
screen.bind("<Down>", player2_down)

while True:
    canvas.update()
    
    ball.setx(ball.xcor() + ball_mx)
    ball.sety(ball.ycor() + ball_my)
    if ball.xcor() >= 300 or ball.xcor() <= -300:
        ball.setx(0)
    if ball.ycor() >= 250 or ball.ycor() <= -250:
        ball_my *= -1

    if player1.distance(ball) <= 25:
        ball_mx *= -1

    if player2.distance(ball) <= 25:
        ball_mx *= -1
screen.mainloop()
