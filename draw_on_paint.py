import pyautogui
import win32api, win32con
from PIL import Image
import numpy as np
import time

image_dir = input("enter here image path: ")
img = Image.open(image_dir).copy().convert("1")
img.show()
mat = np.array(img.getdata()).reshape(img.size)
input("press enter and then you have 5 seconds to move to paint")
time.sleep(5)

def click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.002)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
x = 100
y = 200

for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j] == 0:
            # pyautogui.click(x, y)
            click(x, y)
        x += 1
    y += 1
    x = 100
# C:\Users\Ariel\Desktop\json files and other files\unnamed.png