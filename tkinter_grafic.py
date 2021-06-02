import tkinter

screen = tkinter.Tk()
screen.title("hi!!!")
def say_hi():
    tkinter.Label(screen, text="hi").pack()

btn1 = tkinter.Button(screen, text = "Button1", fg = "red").pack()
btn2 = tkinter.Button(screen, text = "Button2", fg = "green", bg="#0000ff").pack(fill="x")
btn3 = tkinter.Button(screen, text = "Button3", fg = "purple").pack(side = "left")
btn4 = tkinter.Button(screen, text = "Button4", fg = "orange").pack(side = "right", fill="y")
btn4 = tkinter.Button(screen, text = "press me", fg = "gold", command = say_hi).pack()


screen.mainloop()
