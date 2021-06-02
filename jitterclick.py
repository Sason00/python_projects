from pynput.mouse import Button, Controller
import time

mouse = Controller()

print("get ready")
time.sleep(5)

for i in range(5000):
    mouse.press(Button.left)
    mouse.release(Button.left)
    # time.sleep(0.05)
