import cv2
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
cap = cv2.VideoCapture(0)
lmain = tk.Label(screen)
lmain.pack()


def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(10, show_frame)


def cupture_image():
    _, frame = cap.read()
    cv2.imwrite(filename='saved_img.jpg', img=frame)
    # cap.release()


def record_video():
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("saved_video", fourcc, 30, (640, 480))
    tk.Label(screen, text="press q to end the video").pack()
    while True:
        _, frame = cap.read()
        out.write(frame)
        if cv2.waitKey(1 and 0xFF == ord("q")):
            cap.release()
            break


show_frame()
capture_button = ttk.Button(screen, text="capture", command=cupture_image)
capture_button.pack()
record_button = ttk.Button(screen, text="record", command=record_video)
record_button.pack()
screen.mainloop()
