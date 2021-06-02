import turtle
import time
import random

screen = turtle.Screen()
screen.setup(700, 700)
screen.tracer(0)

dots = []
num = 150
clicks = 0
shame_score = 0


def random_points():
    random_x = random.randint(-325, 325)
    random_y = random.randint(-325, 325)
    if times % num == 0:
        new_dot = turtle.Turtle()
        new_dot.shape("circle")
        new_dot.penup()
        new_dot.goto(random_x, random_y)
        new_dot.color(random.choice(["red", "green", "blue", "black"]))
        dots.append(new_dot)


def clicked(x, y):
    global clicks
    global num
    global shame_score
    for i in dots:
        if (i.xcor() < x + 15 and i.xcor() > x - 15) and (i.ycor() < y + 15 and i.ycor() > y - 15):
            i.hideturtle()
            dots.remove(i)
            clicks += 1
            if clicks >= 20:
                if clicks % 10 == 0:
                    num -= 10
        else:
            shame_score += 1


write_times = turtle.Turtle()
write_hits = turtle.Turtle()
write_shame_score = turtle.Turtle()


def write_score():
    global write_times
    global write_hits
    global write_shame_score
    write_times.speed(0)
    write_times.penup()
    write_times.goto(-290, 320)
    write_times.hideturtle()
    write_times.clear()
    write_times.write("your score: " + str(int(times / 10)),
                      align="Center", font=("Arial", 10, "normal"))

    write_hits.speed(0)
    write_hits.penup()
    write_hits.goto(-0, 320)
    write_hits.hideturtle()
    write_hits.clear()
    write_hits.write("your hits: " + str(clicks),
                     align="Center", font=("Arial", 10, "normal"))

    write_shame_score.speed(0)
    write_shame_score.penup()
    write_shame_score.goto(290, 320)
    write_shame_score.hideturtle()
    write_shame_score.clear()
    write_shame_score.write("your misses: " + str(shame_score),
                            align="Center", font=("Arial", 10, "normal"))


screen.listen()
screen.onclick(clicked)

times = 0
while True:
    screen.update()
    random_points()
    times += 1
    write_score()

    if len(dots) >= 50:
        print("kind of gameover")

    time.sleep(0.005)
