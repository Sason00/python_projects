import turtle
from time import sleep

screen = turtle.Screen()
screen.setup(500, 500)
screen.bgcolor("black")
screen.tracer(0)

boxes = []
boxes_x = -200
boxes_y = 200
corrent_turn = "p"  # "p" is player and "c" is computer
clicked_boxes = []
moves_order = []
board = [None, None, None,
         None, None, None,
         None, None, None
         ]

for i in range(1, 10):
    print(i)
    box = turtle.Turtle()
    box.shape("square")
    box.color("white")
    box.shapesize(stretch_len=9, stretch_wid=9)
    box.penup()
    box.speed(0)
    if i == 1 or i == 4 or i == 7:
        box.setpos(boxes_x, boxes_y)
        boxes_x += 196
    elif i == 2 or i == 5 or i == 8:
        box.setpos(boxes_x, boxes_y)
        boxes_x += 196
    elif i == 3 or i == 6 or i == 9:
        box.setpos(boxes_x, boxes_y)
        boxes_x = -200
        boxes_y -= 196
    boxes.append(box)


def check_clicks(num=None):
    global moves_order
    global corrent_turn
    global board
    global pen1
    pen1 = turtle.Turtle()
    pen1.hideturtle()
    pen1.penup()

    if type(num) == int and corrent_turn == "p":
        if boxes[num] in clicked_boxes:
            return
        else:
            pen1.goto(boxes[num].xcor(), boxes[num].ycor())
            boxes[num].color("blue")
            #pen1.write("X", font=("Arial", 16, "normal"))
            clicked_boxes.append(boxes[num])
            board[num] = "X"

        corrent_turn = "c"


def computer_move():
    global corrent_turn
    for i in range(len(board) - 1):
        if board[i] == None:
            board[i] = "O"
            pen1.goto(boxes[i].xcor(), boxes[i].ycor())
            boxes[i].color("red")
            #pen1.write("O", font=("Arial", 16, "normal"))
            clicked_boxes.append(boxes[i])
            board[i] = "O"

            corrent_turn = "p"
            print(board)
            return


screen.listen()
boxes[0].onclick(lambda x, y: check_clicks(0))
boxes[1].onclick(lambda x, y: check_clicks(1))
boxes[2].onclick(lambda x, y: check_clicks(2))
boxes[3].onclick(lambda x, y: check_clicks(3))
boxes[4].onclick(lambda x, y: check_clicks(4))
boxes[5].onclick(lambda x, y: check_clicks(5))
boxes[6].onclick(lambda x, y: check_clicks(6))
boxes[7].onclick(lambda x, y: check_clicks(7))
boxes[8].onclick(lambda x, y: check_clicks(8))
while True:
    screen.update()

    for i in clicked_boxes:
        if i == "X":
            pen1.goto(i.xcor(), i.ycor())
            boxes[i].color("blue")
            print("X")
        elif i == "O":
            pen1.goto(i.xcor(), i.ycor())
            boxes[i].color("red")
            print("O")

    if corrent_turn == "c":
        computer_move()

    sleep(0.5)
