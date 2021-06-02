import tkinter as tk
import webbrowser

screen = tk.Tk()

btn1 = tk.Button(screen, text="google",
                 command=lambda: webbrowser.open_new("http://www.google.com"))
btn1.pack()
btn2 = tk.Button(screen, text="apple",
                 command=lambda: webbrowser.open_new("http://www.apple.com"))
btn2.pack()
btn3 = tk.Button(screen, text="youtube",
                 command=lambda: webbrowser.open_new("http://www.youtube.com"))
btn3.pack()
screen.mainloop()
