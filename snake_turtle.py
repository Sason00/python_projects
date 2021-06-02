import turtle
import time
import random

gameover = False

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.penup()
player_direction = "up"
player_dx = 20
player_dy = 20
tails = []

player_score = 0


def random_x():
    point_x = int(random.randrange(-28, 28))
    return point_x * 10


def random_y():
    point_y = int(random.randrange(-28, 28))
    return point_y * 10


def create_apple():
    global apple
    apple = turtle.Turtle()
    apple.penup()
    apple.speed(0)
    apple.shape("square")
    apple.color("red")
    apple.goto(random_x(), random_y())


create_apple()


def player_move():
    global player_direction
    if player_direction == "right":
        player.setx(player.xcor() + player_dx)
    if player_direction == "left":
        player.setx(player.xcor() - player_dx)
    if player_direction == "up":
        player.sety(player.ycor() + player_dy)
    if player_direction == "down":
        player.sety(player.ycor() - player_dy)


def move_left():
    global player_direction
    if player_direction == "right":
        pass
    else:
        player_direction = "left"
    print(player_direction)


def move_right():
    global player_direction
    if player_direction == "left":
        pass
    else:
        player_direction = "right"
    print(player_direction)


def move_up():
    global player_direction
    if player_direction == "down":
        pass
    else:
        player_direction = "up"
    print(player_direction)


def move_down():
    global player_direction
    if player_direction == "up":
        pass
    else:
        player_direction = "down"
    print(player_direction)


def write_score():
    global score
    score = turtle.Turtle()
    score.speed(0)
    score.penup()
    score.goto(0, 260)
    score.hideturtle()
    score.write("Score: " + str(player_score), align="Center",
                font=("Arial", 15, "normal"))


def gameOver():
    global tails
    global player_score
    player.setx(0)
    player.sety(0)
    player_score = 0
    score.clear()
    write_score()
    for t in tails:
        t.hideturtle()
    tails = []


write_score()

screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")

while not gameover:
    screen.update()

    if player.xcor() >= 300 or player.xcor() <= -300 or player.ycor() >= 300 or player.ycor() <= -300:
        #gameover = True
        #print("game over!")
        gameOver()

    for j in tails:
        if j.distance(player) < 20:
            #gameover = True
            #print("game over!")
            gameOver()

    if apple.distance(player) < 20:
        print("hi")
        apple.hideturtle()
        create_apple()
        player_score += 1
        score.clear()
        write_score()

        new_tail = turtle.Turtle()
        new_tail.speed(0)
        new_tail.penup()
        new_tail.color("green")
        new_tail.shape("square")
        tails.append(new_tail)

    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)

    if len(tails) > 0:
        x = player.xcor()
        y = player.ycor()
        tails[0].goto(x, y)

    player_move()
    time.sleep(0.123)
