import random

board = [[" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "]]
level = 2
gameover = False
times1 = 0

def place_random_number(b):
    placed = False
    while not placed:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if b[y][x] == " ":
            b[y][x] = str(level)
            placed = True

def move_up(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            y = i
            x = j
            try:
                while b[y][x] != " ":
                    if y > 0:
                        if b[y - 1][x] == " ":
                            b[y - 1][x] = b[y][x]
                            b[y][x] = " "
                        elif b[y - 1][x] == b[y][x]:
                            b[y - 1][x] = str(int(b[y][x]) * 2)
                            b[y][x] = " "
                            break
                    y -= 1
            except:
                pass

def move_down(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            y = i
            x = j
            try:
                while b[y][x] != " ":
                    if y < 3:
                        if b[y + 1][x] == " ":
                            b[y + 1][x] = b[y][x]
                            b[y][x] = " "
                        elif b[y + 1][x] == b[y][x]:
                            b[y + 1][x] = str(int(b[y][x]) * 2)
                            b[y][x] = " "
                            break
                    y += 1
            except:
                pass


def move_left(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            y = i
            x = j
            try:
                while b[y][x] != " ":
                    if x > 0:
                        if b[y][x - 1] == " ":
                            b[y][x - 1] = b[y][x]
                            b[y][x] = " "
                        elif b[y][x - 1] == b[y][x]:
                            b[y][x - 1] = str(int(b[y][x]) * 2)
                            b[y][x] = " "
                            break
                    x -= 1
            except:
                pass

def move_right(b):
    for i in range(0, len(b)):
        for j in range(0, len(b[i])):
            y = i
            x = j
            try:
                while b[y][x] != " ":
                    if x < 3:
                        if b[y][x + 1] == " ":
                            b[y][x + 1] = b[y][x]
                            b[y][x] = " "
                        elif b[y][x + 1] == b[y][x]:
                            b[y][x + 1] = str(int(b[y][x]) * 2)
                            b[y][x] = " "
                            break
                    x += 1
            except:
                pass

def print_board(b):
    print("-" * 17)
    for i in b:
        print("|", i[0], "|", i[1], "|", i[2], "|", i[3], "|")
        print("-" * 17)

while not gameover:
    place_random_number(board)
    print_board(board)
    move = input('press "w" for up, "s" for down, "a" for left, "d" for right: ')
    while not move in ("w", "s", "a", "d"): 
        move = input('press "w" for up, "s" for down, "a" for left, "d" for right: ')
    if move == "w":
        move_up(board)
    elif move == "s":
        move_down(board)
    elif move == "a":
        move_left(board)
    elif move == "d":
        move_right(board)
    times1 += 1
    if times1 % 10 == 0:
        level *= 2 