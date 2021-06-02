import turtle
import time
import random
import tkinter as tk
from tkinter import ttk

screen = turtle.Screen()
screen.tracer(0)
screen.setup(700, 700, 500, 50)
s = screen._root
frame1 = tk.Frame(s)
frame1.pack()
frame2 = tk.Frame(frame1)
frame2.pack(side=tk.LEFT, fill=tk.Y, expand=True)
pick_player = ttk.Combobox(frame2, values=("Normal", "Sniper", "Minigun"), textvariable=tk.StringVar())
pick_player.current(0)
pick_player.pack()
hp_bar = ttk.Progressbar(frame1, orient = tk.HORIZONTAL, length=100)
hp_bar.pack(ipadx=100)
money_bar = tk.Label(frame1, text="money: ")
money_bar.pack(side=tk.LEFT)

gameover = False
board = [[-344.0, -7.0], [-331.0, -7.0], [-320.0, -8.0], [-305.0, -5.0], [-296.0, -5.0], [-286.0, -6.0], [-279.0, -5.0], [-266.0, -6.0], [-254.0, -5.0], [-243.0, -5.0], [-236.0, -4.0], [-227.0, -6.0], [-216.0, -6.0], [-208.0, -6.0], [-206.0, 4.0], [-207.0, 17.0], [-207.0, 32.0], [-211.0, 44.0], [-210.0, 64.0], [-208.0, 77.0], [-212.0, 96.0], [-210.0, 114.0], [-210.0, 125.0], [-210.0, 137.0], [-210.0, 143.0], [-211.0, 149.0], [-211.0, 158.0], [-211.0, 168.0], [-212.0, 181.0], [-213.0, 195.0], [-213.0, 212.0], [-214.0, 225.0], [-214.0, 238.0], [-213.0, 255.0], [-211.0, 268.0], [-197.0, 273.0], [-183.0, 271.0], [-171.0, 270.0], [-157.0, 273.0], [-142.0, 271.0], [-128.0, 269.0], [-111.0, 265.0], [-98.0, 266.0], [-97.0, 255.0], [-96.0, 240.0], [-95.0, 223.0], [-94.0, 209.0], [-96.0, 193.0], [-96.0, 179.0], [-96.0, 164.0], [-96.0, 144.0], [-96.0, 130.0], [-94.0, 115.0], [-96.0, 96.0], [-94.0, 78.0], [-94.0, 61.0], [-95.0, 43.0], [-96.0, 28.0], [-96.0, 10.0], [-95.0, -8.0], [-94.0, -29.0], [-96.0, -42.0], [-96.0, -59.0], [-97.0, -72.0], [-99.0, -89.0], [-100.0, -104.0], [-99.0, -122.0], [-96.0, -138.0], [-99.0, -158.0], [-99.0, -174.0], [-98.0, -193.0], [-100.0, -208.0], [-100.0, -227.0], [-101.0, -248.0], [-99.0, -266.0], [-80.0, -271.0], [-58.0, -270.0], [-39.0, -269.0], [-39.0, -254.0], [-24.0, -255.0], [-17.0, -237.0], [-4.0, -234.0], [-2.0, -215.0], [-4.0, -197.0], [-9.0, -181.0], [-10.0, -164.0], [-9.0, -149.0], [-10.0, -133.0], [-13.0, -116.0], [-14.0, -101.0], [-15.0, -82.0], [-14.0, -59.0], [-9.0, -41.0], [-1.0, -28.0], [1.0, -16.0], [1.0, 3.0], [1.0, 17.0], [1.0, 36.0], [0.0, 54.0], [0.0, 68.0], [1.0, 84.0], [2.0, 102.0], [1.0, 119.0], [2.0, 140.0], [5.0, 154.0], [5.0, 178.0], [4.0, 195.0], [4.0, 208.0], [4.0, 219.0], [4.0, 232.0], [6.0, 250.0], [12.0, 267.0], [25.0, 265.0], [37.0, 261.0], [46.0, 253.0], [53.0, 243.0], [61.0, 230.0], [67.0, 217.0], [74.0, 205.0], [80.0, 189.0], [87.0, 172.0], [93.0, 156.0], [98.0, 143.0], [103.0, 128.0], [108.0, 114.0], [117.0, 97.0], [120.0, 83.0], [124.0, 68.0], [128.0, 55.0], [134.0, 42.0], [139.0, 27.0], [150.0, 24.0], [157.0, 18.0], [166.0, 8.0], [181.0, 4.0], [198.0, 3.0], [219.0, -1.0], [235.0, -2.0], [251.0, -4.0], [267.0, -5.0], [285.0, -6.0], [301.0, -6.0], [318.0, -8.0], [333.0, -9.0]]
baloons = []
towers = []
hp = 5
hp_bar["value"] = (hp * 20)
money = 50
money_bar["text"] = "money: " + str(money) + "$"
num_of_blaoons = 0

board_way = turtle.Turtle()
board_way.penup()
board_way.goto(board[0][0], board[0][1])
board_way.pendown()
for i in board:
    board_way.goto(i[0], i[1])
board_way.hideturtle()
del board_way

class baloon:
    def __init__(self,level=1 ,x = 0, y = 0):
        if level > 4:
            self.level = 1
        elif level <= 0:
            return
        else:
            self.level = level
        self.x = x
        self.y = y
        self.Baloon = turtle.Turtle()
        self.Baloon.penup()
        self.Baloon.shape("circle")
        self.Baloon.setx(self.x)
        self.Baloon.sety(self.y)
        self.counter = 0
        if self.level == 1:
            self.Baloon.color("red")
        elif self.level == 2:
            self.Baloon.color("green")
        elif self.level == 3:
            self.Baloon.color("blue")
        elif self.level == 4:
            self.Baloon.color("yellow")

    def setx(self, x):
        self.Baloon.setx(x)

    def sety(self, y):
        self.Baloon.sety(y)

    def goto(self, x, y):
        self.Baloon.goto(x, y)
    
    def getx(self):
        return self.Baloon.xcor()

    def gety(self):
        return self.Baloon.ycor()

    def getcoors(self):
        return (self.getx(), self.gety())

    def update(self):
        if self.level == 1:
            self.Baloon.color("red")
        elif self.level == 2:
            self.Baloon.color("green")
        elif self.level == 3:
            self.Baloon.color("blue")
        elif self.level == 4:
            self.Baloon.color("yellow")
        elif self.level <= 0:
            self.delete() 
    
    def delete(self):
        self.Baloon.hideturtle()
        del self.Baloon
    
class tower:
    def __init__(self, _type="normal", x=0, y=0):
        self._type = _type
        self.x = x
        self.y = y
        self.cooldown = 0
        self.Tower = turtle.Turtle()
        self.Tower.penup()
        self.Tower.shape("square")
        self.Tower.setx(self.x)
        self.Tower.sety(self.y)
        if self._type == "normal":
            self.Tower.color("black")
        elif self._type == "sniper":
            self.Tower.color("green")
        elif self._type == "minigun":
            self.Tower.color("brown")

    def shoot(self):
        if self._type == "normal":
            if self.cooldown >= 10:
                self.cooldown = 0
                for j in baloons:
                    if self.Tower.distance(j.Baloon) <= 100:
                        #print("close")
                        j.level -= 1
                        j.update()
                        if j.level <= 0:
                            baloons.remove(j)
                            return (True, True)
                return (True, False)
            return (False, False)
        elif self._type == "sniper":
            if self.cooldown >= 30:
                self.cooldown = 0
                for j in baloons:
                    if self.Tower.distance(j.Baloon) <= 7000:
                        j.level -= 1
                        j.update()
                        if j.level <= 0:
                            baloons.remove(j)
                            return (True, True)
                return (True, False)
            return (False, False)
        elif self._type == "minigun":
            if self.cooldown >= 3:
                self.cooldown = 0
                for j in baloons:
                    if self.Tower.distance(j.Baloon) <= 40:
                        j.level -= 1
                        j.update()
                        if j.level <= 0:
                            baloons.remove(j)
                            return (True, True)
                return (True, False)
            return (False, False)


def place_tower(x, y):
    global money
    if money >= 25 and pick_player.get() == "Normal":
        t = tower(_type="normal", x=x, y=y)
        towers.append(t)
        screen.update()
        money -= 25
        money_bar["text"] = "money: " + str(money) + "$"
    elif money >= 30 and pick_player.get() == "Sniper":
        t = tower(_type="sniper", x=x, y=y)
        towers.append(t)
        screen.update()
        money -= 30
        money_bar["text"] = "money: " + str(money) + "$"
    elif money >= 35 and pick_player.get() == "Minigun":
        t = tower(_type="minigun", x=x, y=y)
        towers.append(t)
        screen.update()
        money -= 35
        money_bar["text"] = "money: " + str(money) + "$"
    print(pick_player.get())

wave_counter = 0
baloon_counter = 0

screen.listen()
screen.onclick(place_tower, btn=1)
while not gameover:
    screen.update()

    for i in baloons:
        if i.getcoors()[0] >= board[-1][0] and i.getcoors()[1] >= board[-1][1]:
            i.counter = 0
            i.delete()
            baloons.remove(i)
            hp -= 1
            hp_bar["value"] = (hp * 20)
            if hp <= 0:
                gameover = True
        else:
            try:
                i.goto(board[i.counter][0], board[i.counter][1])
                i.counter += 1
            except:
                pass

    
    for i in towers:
        i.cooldown += 1
        s = i.shoot()
        if s[1]:
            money += [2.5, 0.5][random.randint(0, 1)]
            money_bar["text"] = "money: " + str(money) + "$"
    """
    if baloon_counter == 10:
        b = baloon(level=3, x=-344.0, y=-7.0)
        baloons.append(b)
        num_of_blaoons += 1
        baloon_counter = 0

    if baloon_counter = 0:
        wave_counter += 1

    baloon_counter += 1
    """
    if wave_counter == 0:
        if baloon_counter == 10:
            b = baloon(level=1, x=-344.0, y=-7.0)
            baloons.append(b)
            num_of_blaoons += 1
            baloon_counter = 0

        else:
            baloon_counter += 1
        
        if num_of_blaoons >= 3:
            wave_counter += 1
            num_of_blaoons = 0

    elif wave_counter == 1:
        if baloon_counter == 10:
            b = baloon(level=[1, 2][num_of_blaoons%2==1], x=-344.0, y=-7.0)
            baloons.append(b)
            num_of_blaoons += 1
            baloon_counter = 0

        else:
            baloon_counter += 1
            
        if num_of_blaoons >= 10:
            wave_counter += 1
            num_of_blaoons = 0

    elif wave_counter == 2:
        if baloon_counter == 7:
            b = baloon(level=2, x=-344.0, y=-7.0)
            baloons.append(b)
            num_of_blaoons += 1
            baloon_counter = 0

        else:
            baloon_counter += 1
            
        if num_of_blaoons >= 25:
            wave_counter += 1
            num_of_blaoons = 0
        
    elif wave_counter == 3:
        if baloon_counter == 5:
            b = baloon(level=[1, 3][num_of_blaoons%2==1], x=-344.0, y=-7.0)
            baloons.append(b)
            num_of_blaoons += 1
            baloon_counter = 0

        else:
            baloon_counter += 1
            
        if num_of_blaoons >= 25:
            wave_counter += 1
            num_of_blaoons = 0

    elif wave_counter == 4:
        if baloon_counter == 1:
            b = baloon(level=3, x=-344.0, y=-7.0)
            baloons.append(b)
            num_of_blaoons += 1
            baloon_counter = 0

        else:
            baloon_counter += 1
            
        if num_of_blaoons >= 100:
            wave_counter += 1
            num_of_blaoons = 0

    elif wave_counter == 5:
        if baloon_counter == 1:
            b = baloon(level=[3, 4][num_of_blaoons%2==0], x=-344.0, y=-7.0)
            baloons.append(b)
            num_of_blaoons += 1
            baloon_counter = 0

        else:
            baloon_counter += 1
            
        if num_of_blaoons >= 20:
            wave_counter += 1
            num_of_blaoons = 0

    time.sleep(0.05)