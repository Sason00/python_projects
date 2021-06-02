import turtle
import time
import random

screen = turtle.Screen()
screen.setup(450, 550)
screen.bgcolor("black")
screen.tracer(0)

bullets = []
enemys = []
enemy_bullets = []
lives = 3
life = 5
score = 0
is_left = False
is_right = False
print("your life:", lives)
print("player hp:", life)

player = turtle.Turtle()
player.penup()
player.shape("arrow")
player.color("white")
player.shapesize(stretch_wid=2, stretch_len=6)
player.left(90)
player.goto(0, -260)

pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.hideturtle()
pen.goto(-220, 250)
pen.write("your life: " + str(lives) + "\t" + "your hp: " +
          str(life) + "\t" + "score: " + str(score), font=("Arial", 15, "normal"))

for i in range(20):
    stars = turtle.Turtle()
    stars.penup()
    stars.shape("square")
    stars.color("white")
    stars.shapesize(stretch_wid=0.2, stretch_len=0.2)
    stars.goto(random.randrange(-170, 170), random.randrange(-250, 250))


def move_left():
    global is_left
    is_left = True


def move_right():
    global is_right
    is_right = True


def move_left2():
    global is_left
    is_left = False


def move_right2():
    global is_right
    is_right = False


def shoot():
    bullet = turtle.Turtle()
    bullet.penup()
    bullet.shape("square")
    bullet.color("red")
    bullet.shapesize(stretch_wid=2, stretch_len=0.2)
    bullet.goto(player.xcor(), player.ycor() + 50)
    bullets.append(bullet)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeyrelease(move_left2, "Left")
screen.onkeyrelease(move_right2, "Right")
screen.onkeyrelease(shoot, "space")
while True:
    screen.update()

    if is_left:
        player.setx(player.xcor() - 7)
        if player.xcor() <= -225:
            player.setx(-225)
    if is_right:
        player.setx(player.xcor() + 7)
        if player.xcor() >= 225:
            player.setx(225)

    for i in bullets:
        i.sety(i.ycor() + 5)

        for j in enemys:
            if i.distance(j) <= 40:
                j.hideturtle()
                enemys.remove(j)
                score += 1

        if i.ycor() >= 275:
            i.hideturtle()
            bullets.remove(i)

    if random.choice([i for i in range(140)]) == 1:
        e = turtle.Turtle()
        e.shape("arrow")
        e.color("gray")
        e.shapesize(stretch_wid=1, stretch_len=6)
        e.right(90)
        e.penup()
        e.goto(random.randrange(-220, 220), 260)
        enemys.append(e)

    for i in enemys:
        i.sety(i.ycor() - 1)
        if i.ycor() <= -275:
            i.hideturtle()
            enemys.remove(i)
            lives -= 1
            print("your life:", lives)

    if lives <= 0:
        print("game over")
        screen.bye()
        break

    if random.choice([i for i in range(100)]) == 1:
        try:
            chosen_enemy = random.choice(enemys)
            enemy_bullet = turtle.Turtle()
            enemy_bullet.penup()
            enemy_bullet.shape("square")
            enemy_bullet.color("green")
            enemy_bullet.shapesize(stretch_wid=2, stretch_len=0.2)
            enemy_bullet.goto(chosen_enemy.xcor(), chosen_enemy.ycor())
            enemy_bullets.append(enemy_bullet)
        except:
            pass
    for i in enemy_bullets:
        i.sety(i.ycor() - 5)
        if i.ycor() <= -275:
            i.hideturtle()
            enemy_bullets.remove(i)
            if i.distance(player) <= 40:
                life -= 1
                print("player hp:", life)
    if life <= 0:
        print("game over")
        screen.bye()
        break

    pen.clear()
    pen.write("your life: " + str(lives) + "\t" + "your hp: " +
              str(life) + "\t" + "score: " + str(score), font=("Arial", 15, "normal"))

    time.sleep(0.0001)
