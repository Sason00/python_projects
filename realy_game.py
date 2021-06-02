import turtle
import time
from multiprocessing import Process

screen = turtle.Screen()
screen.setup(800, 500)
screen.tracer(0)

player_shape = "/Users/rylwrn/Desktop/python_projects/realy_game photos & files/player.gif"
screen.addshape(player_shape)
player = turtle.Turtle()
player.shape(player_shape)
player.penup()
player.goto(-340, 10)

blocks = []
is_level_one_started = False
is_jumping = False
times = 0


class block:

    def __init__(self, position, block_image="/Users/rylwrn/Desktop/python_projects/realy_game photos & files/diffult_block.gif"):
        screen.addshape(block_image)
        self.new_block = turtle.Turtle()
        self.new_block.shape(block_image)
        self.new_block.penup()
        self.new_block.goto(position[0], position[1])
        blocks.append(self.new_block)


def level_one():
    global is_level_one_started
    if not is_level_one_started:
        is_level_one_started = True
        block(position=(250, -300))
        block(position=(277, -273))
        block(position=(305, -273))
        block(position=(333, -246))


def player_gravity():
    if player.ycor() <= -220:
        player.sety(-220)
    else:
        player.sety(player.ycor() - 10)


def forward():
    try:
        for i in blocks:
            i.setx(i.xcor() - 10)
    except:
        pass


def backward():
    try:
        for i in blocks:
            i.setx(i.xcor() + 10)
    except:
        pass


def jump():
    player.sety(player.ycor() + 200)
    try:
        for i in blocks:
            i.setx(i.xcor() - 10)
    except:
        pass
    print("jump")
    time.sleep(0.2)


screen.listen()
screen.onkeypress(forward, "d")
screen.onkeypress(backward, "a")
screen.onkeypress(jump, "space")

while True:
    times += 1
    screen.update()
    player_gravity()
    if not is_level_one_started:
        level_one()
    try:
        if player.xcor() >= (blocks[3].xcor() + 15):
            print("you finished level one seccesfuly")
            blocks = []
    except:
        pass
    time.sleep(0.005)
