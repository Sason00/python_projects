import turtle
import time
import random
import json

screen = turtle.Screen()
screen.setup(600, 500)
screen.bgcolor("black")
screen.tracer(0)

player = turtle.Turtle()
player.color("orange")
player.shape("square")
player.speed(0)
player.penup()

pen_score = turtle.Turtle()
pen_score.hideturtle()
pen_score.speed(0)
pen_score.penup()
pen_score.color("white")
pen_score.goto(0, 230)

pen_last_score = turtle.Turtle()
pen_last_score.hideturtle()
pen_last_score.speed(0)
pen_last_score.penup()
pen_last_score.color("white")
pen_last_score.goto(-225, 230)

pen_best_score = turtle.Turtle()
pen_best_score.hideturtle()
pen_best_score.speed(0)
pen_best_score.penup()
pen_best_score.color("white")
pen_best_score.goto(225, 230)

balls = []
balls_dirs = []
times = 0
gameover = False
json_file = json.load(
    open("C:\\Users\\Ariel\\Desktop\\json files\\kind_of_game_json.json"))


def create_balls():
    global balls
    global balls_dirs
    ball = turtle.Turtle()
    ball.color("red")
    ball.shape("square")
    ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
    ball.speed(0)
    ball.penup()
    balls.append(ball)
    balls_dirs.append([5 * random.choice((1, -1)),
                       7 * random.choice((1, -1))])


def score():
    global times
    global pen_score
    global pen_last_score
    global pen_best_score
    global json_file
    times += 0.5
    if times % 78 == 0:
        create_balls()
    pen_last_score.clear()
    pen_last_score.write("your last score is: " + str(json_file["last_score"]), align="center",
                         font=("Arial", 8, "normal"))
    pen_score.clear()
    pen_score.write("your score is: " + str(int(times / 10)), align="Left",
                    font=("Arial", 8, "normal"))
    pen_best_score.clear()
    pen_best_score.write("your best score is: " + str(json_file["best_score"]), align="center",
                         font=("Arial", 8, "normal"))


def dragging(x, y):
    player.goto(x, y)
    player.ondrag(dragging)


def go_to(x, y):
    player.goto(x, y)


screen.listen()
screen.onclick(go_to)
player.ondrag(dragging)

while not gameover:
    screen.update()
    if player.xcor() > 300:
        player.setx(300)
    elif player.xcor() < -300:
        player.setx(-300)
    elif player.ycor() > 250:
        player.sety(250)
    elif player.ycor() < -250:
        player.sety(-250)

    for i in range(len(balls)):
        balls[i].setx(balls[i].xcor() + balls_dirs[i][0] * -1)
        balls[i].sety(balls[i].ycor() + balls_dirs[i][1] * -1)
        if balls[i].xcor() >= 300:
            balls_dirs[i][0] *= -1
        elif balls[i].xcor() <= -300:
            balls_dirs[i][0] *= -1
        elif balls[i].ycor() >= 250:
            balls[i].sety(balls[i].ycor() - 10)
            balls_dirs[i][1] *= -1
        elif balls[i].ycor() <= -250:
            balls[i].sety(balls[i].ycor() + 10)
            balls_dirs[i][1] *= -1

    for i in balls:
        if player.distance(i) < 15:
            for f in balls:
                f.hideturtle()
            balls = []
            balls_dirs = []
            json_file["last_score"] = int(times/10)
            json_file["scores"].append(times)
            json_file["best_score"] = int(max(json_file["scores"])/10)
            times = 0
            print("game over")
            time.sleep(1)
    score()
    time.sleep(0.005)
