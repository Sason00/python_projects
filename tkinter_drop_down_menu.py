import tkinter
import tkinter.messagebox

screen = tkinter.Tk()

def prt():
    print("hi")

def alert():
    tkinter.messagebox.showinfo("alert message", "it is alert message")

def question():
    q = tkinter.messagebox.askquestion("question", "do you like python?")
    if q == 1:
        tkinter.Label(screen, text="you like python").pack()
    elif q == 2:
        tkinter.Label(screen, text="you don't like python").pack()

menu = tkinter.Menu(screen)
screen.config(menu = menu)
file_menu_1 = tkinter.Menu(menu)
example_1 = menu.add_cascade(label = "example 1", menu = file_menu_1)
file_menu_1.add_command(label = "it will print hi", command = prt)
file_menu_2 = tkinter.Menu(menu)
alerts = menu.add_cascade(label = "alerts", menu = file_menu_2)
file_menu_2.add_command(label = "it will alert", command = alert)
file_menu_2.add_command(label = "it will ask you a question", command = question)

screen.mainloop()