import turtle
import time
import tkinter.messagebox
import random

game_over = False

screen_width = 800
screen_height = 600
screen = turtle.Screen()
screen.title("Pong")
screen.setup(width=screen_width, height=screen_height)
screen.tracer(0)

paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.penup()
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.goto(-350, 0)

paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.penup()
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2

score_1 = 0
score_2 = 0


def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    if y > 250:
        y = 250
    paddle_2.sety(y)


def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    if y < -250:
        y = -250
    paddle_2.sety(y)


def write_score():
    global score
    score = turtle.Turtle()
    score.speed(0)
    score.penup()
    score.goto(0, 260)
    score.hideturtle()
    score.write("Player 1: " + str(score_1) + "  Player 2: " + str(score_2),
                align="Center", font=("Arial", 15, "normal"))
    if score_1 == 10:
        tkinter.messagebox.showinfo("game over", "Player 1 won")
        game_over = True
        screen.close()

    if score_2 == 10:
        tkinter.messagebox.showinfo("game over", "Player 2 won")
        game_over = True
        screen.close()


write_score()

screen.listen()
screen.onkeypress(paddle_2_up, "Up")
screen.onkeypress(paddle_2_down, "Down")

counter = 0
while not game_over:
    screen.update()
    counter += 1
    #if counter >= 10:
    #    if random.random() > 0.6:
    paddle_1.sety(ball.ycor())
        #counter = 0

    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_1 += 1
        score.clear()
        write_score()

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_2 += 1
        score.clear()
        write_score()

    if ball.xcor() > 340 and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        print("hi")

    if ball.xcor() < -340 and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        print("hii")
    time.sleep(0.000001)

