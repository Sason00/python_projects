import os
import pyautogui
import time

os.chdir(r"C:\Users\Ariel\AppData\Roaming\Zoom\bin")
os.startfile("Zoom.exe")

time.sleep(1)

button_cords = pyautogui.locateOnScreen(
    r"C:\Users\Ariel\Desktop\json files and other files\Capture.PNG", confidence=0.9)
pyautogui.moveTo(button_cords.left + 5, button_cords.top + 5)
time.sleep(0.01)
pyautogui.click()
# C:\Users\Ariel\Desktop\json files and other files\Capture3.PNG

button_cords2 = pyautogui.locateOnScreen(
    r"C:\Users\Ariel\Desktop\json files and other files\Capture3.PNG", confidence=0.9)
while not button_cords2:
    button_cords2 = pyautogui.locateOnScreen(
        r"C:\Users\Ariel\Desktop\json files and other files\Capture3.PNG", confidence=0.9)
pyautogui.moveTo(button_cords2.left + 5, button_cords2.top + 5)
time.sleep(0.001)
pyautogui.click()

button_cords4 = pyautogui.locateOnScreen(
    r"C:\Users\Ariel\Desktop\json files and other files\Capture4.PNG", confidence=0.9)
while not button_cords4:
    button_cords2 = pyautogui.locateOnScreen(
        r"C:\Users\Ariel\Desktop\json files and other files\Capture4.PNG", confidence=0.9)
pyautogui.moveTo(button_cords4.left + 5, button_cords4.top + 5)
time.sleep(0.01)
pyautogui.click()


button_cords3 = pyautogui.locateOnScreen(
    r"C:\Users\Ariel\Desktop\json files and other files\Capture2.PNG", confidence=0.9)
while not button_cords3:
    button_cords3 = pyautogui.locateOnScreen(
        r"C:\Users\Ariel\Desktop\json files and other files\Capture2.PNG", confidence=0.9)
pyautogui.moveTo(button_cords3.left + 5, button_cords3.top + 5)
time.sleep(0.001)
pyautogui.click()
