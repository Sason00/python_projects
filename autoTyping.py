import os
from time import sleep
from pynput.keyboard import Controller

controller = Controller()

f = open("some.txt", "w")
f.write("")
f.close()
os.system("start some.txt")
sleep(1)
for j in "this is a virus!!!":
    controller.press(j)
    controller.release(j)
    sleep(0.2)

