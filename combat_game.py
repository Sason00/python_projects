import turtle
from time import sleep
import os

screen = turtle.Screen()
screen.setup(700, 400)
screen.tracer(0)

player1_normal_texture = ["\\combat_game_photos\\player1(0).gif", "\\combat_game_photos\\player1(1).gif"]
player1_punch_texture = ["\\combat_game_photos\\player1_punch(0).gif", "\\combat_game_photos\\player1_punch(1).gif"]
player2_normal_texture = ["\\combat_game_photos\\player2(0).gif", "\\combat_game_photos\\player2(1).gif"]
player2_punch_texture = ["\\combat_game_photos\\player2_punch(0).gif", "\\combat_game_photos\\player2_punch(1).gif"]
for i in player1_normal_texture:
    screen.addshape(i)
for i in player1_punch_texture:
    screen.addshape(i)
for i in player2_normal_texture:
    screen.addshape(i)
for i in player2_punch_texture:
    screen.addshape(i)

is_player1_left_clicked = False
is_player1_right_clicked = False
is_player2_left_clicked = False
is_player2_right_clicked = False
player1_jump_cooldown = 0
player2_jump_cooldown = 0
is_player1_can_jump = False
is_player2_can_jump = False
player1_hp = 10
player2_hp = 10
player1_dir = "left"
player2_dir = "right"
player1_attack_cooldown = 0
player2_attack_cooldown = 0

player1 = turtle.Turtle()
player1.penup()
player1.shape(player1_normal_texture[0])
player1.speed(0)
player1.goto(280, -140)
player1.left(90)
player1.shapesize(stretch_wid=4, stretch_len=7)


player2 = turtle.Turtle()
player2.penup()
player2.shape(player2_normal_texture[0])
player2.speed(0)
player2.goto(-280, -140)
player2.left(90)
player2.shapesize(stretch_wid=4, stretch_len=7)


def player1_true_left():
    global is_player1_left_clicked
    global player1_dir
    is_player1_left_clicked = True
    player1.shape(player1_normal_texture[0])
    player1_dir = "left"


def player1_true_right():
    global is_player1_right_clicked
    global player1_dir
    is_player1_right_clicked = True
    player1.shape(player1_normal_texture[1])
    player1_dir = "right"


def player2_true_left():
    global is_player2_left_clicked
    global player2_dir
    is_player2_left_clicked = True
    player2.shape(player2_normal_texture[1])
    player2_dir = "left"


def player2_true_right():
    global is_player2_right_clicked
    global player2_dir
    is_player2_right_clicked = True
    player2.shape(player2_normal_texture[0])
    player2_dir = "right"


def player1_false_left():
    global is_player1_left_clicked
    is_player1_left_clicked = False


def player1_false_right():
    global is_player1_right_clicked
    is_player1_right_clicked = False


def player2_false_left():
    global is_player2_left_clicked
    is_player2_left_clicked = False


def player2_false_right():
    global is_player2_right_clicked
    is_player2_right_clicked = False


def player1_jump():
    global player1_jump_cooldown
    global is_player1_can_jump
    if player1_jump_cooldown >= 80:
        is_player1_can_jump = True
        player1_jump_cooldown = 0

def player2_jump():
    global player2_jump_cooldown
    global is_player2_can_jump
    if player2_jump_cooldown >= 80:
        is_player2_can_jump = True
        player2_jump_cooldown = 0
#
def player1_attack():
    global player2_hp
    global player1_attack_cooldown
    if player1.distance(player2) <= 150:
        player2_hp -= 1
        print("player2 hp:", player2_hp)
    if player1_dir == "right":
        player1.shape(player1_punch_texture[1])
    if player1_dir == "left":
        player1.shape(player1_punch_texture[0])
    player1_attack_cooldown = 0

def player2_attack():
    global player1_hp
    global player2_attack_cooldown
    if player2.distance(player1) <= 150:
        player1_hp -= 1
        print("player1 hp:", player1_hp)
    if player2_dir == "right":
        player2.shape(player2_punch_texture[0])
    if player2_dir == "left":
        player2.shape(player2_punch_texture[1])
    player2_attack_cooldown = 0

screen.listen()
screen.onkeypress(player1_true_right, "Right")
screen.onkeyrelease(player1_false_right, "Right")
screen.onkeypress(player1_true_left, "Left")
screen.onkeyrelease(player1_false_left, "Left")
screen.onkeypress(player2_true_right, "d")
screen.onkeyrelease(player2_false_right, "d")
screen.onkeypress(player2_true_left, "a")
screen.onkeyrelease(player2_false_left, "a")
screen.onkeypress(player1_jump, "Up")
screen.onkeypress(player2_jump, "w")
screen.onkeypress(player1_attack, "0")
screen.onkeypress(player2_attack, "space")
while True:
    screen.update()

    player1_jump_cooldown += 1
    player2_jump_cooldown += 1
    player1_attack_cooldown += 1
    player2_attack_cooldown += 1

    if player1_hp <= 0:
        print("player2 won")
        screen.bye()
    if player2_hp <= 0:
        print("player1 won")
        screen.bye()

    if is_player1_left_clicked:
        player1.setx(player1.xcor() - 5)
    if is_player1_right_clicked:
        player1.setx(player1.xcor() + 5)
    if is_player2_left_clicked:
        player2.setx(player2.xcor() - 5)
    if is_player2_right_clicked:
        player2.setx(player2.xcor() + 5)

    if player1.xcor() >= 340:
        player1.setx(340)
    if player1.xcor() <= -340:
        player1.setx(-340)
    if player2.xcor() >= 340:
        player2.setx(340)
    if player2.xcor() <= -340:
        player2.setx(-340)

    if is_player1_can_jump:
        if player1_jump_cooldown >= 80:
            player1_jump_cooldown = 0
            is_player1_can_jump = False
        if player1_jump_cooldown <= 40:
            player1.sety(player1.ycor() + 5)
        if player1_jump_cooldown > 41:
            player1.sety(player1.ycor() - 5)
    else:
        player1.sety(-140)
    
    if is_player2_can_jump:
        if player2_jump_cooldown >= 80:
            player2_jump_cooldown = 0
            is_player2_can_jump = False
        if player2_jump_cooldown <= 40:
            player2.sety(player2.ycor() + 5)
        if player2_jump_cooldown > 41:
            player2.sety(player2.ycor() - 5)
        
    else:
        player2.sety(-140)
        
    if player1_attack_cooldown >= 20:
        if player1_dir == "left":
            player1.shape(player1_normal_texture[0])
        if player1_dir == "right":
            player1.shape(player1_normal_texture[1])
    if player2_attack_cooldown >= 20:
        if player2_dir == "left":
            player2.shape(player2_normal_texture[1])
        if player2_dir == "right":
            player2.shape(player2_normal_texture[0])

    sleep(0.012)
