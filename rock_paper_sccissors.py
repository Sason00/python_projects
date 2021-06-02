import tkinter as tk

screen = tk.Tk()
screen.configure(bg="black")
screen.geometry("782x565")

frame1 = tk.Frame(screen, bg="black")
frame1.grid(row=0, column=0)
frame2 = tk.Frame(screen, bg="black")
frame2.grid(row=1, column=0)

player_choise = tk.Label(frame1, text="player:",
                         bg="black", fg="white", font=("arial", 24, "bold"))
player_choise.pack()
computer_choise = tk.Label(frame1, text="computer:",
                           bg="black", fg="white", font=("arial", 24, "bold"))
computer_choise.pack()

rock = tk.Button(frame2, text="rock", bg="black",
                 fg="white", font=("arial", 24, "bold"), borderwidth=5)
rock.grid(row=0, column=0)
paper = tk.Button(frame2, text="paper", bg="black",
                  fg="white", font=("arial", 24, "bold"), borderwidth=5)
paper.grid(row=0, column=1)
scissors = tk.Button(frame2, text="scissors", bg="black",
                     fg="white", font=("arial", 24, "bold"), borderwidth=5)
scissors.grid(row=0, column=2)
screen.mainloop()
