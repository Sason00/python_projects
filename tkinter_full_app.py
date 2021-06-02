import tkinter as tk

screen = tk.Tk()

menu = tk.Menu(screen)
screen.config(menu=menu)
screen.geometry("900x600")
file_menu_1 = tk.Menu(menu)
file_menu_2 = tk.Menu(menu)
file_menu_3 = tk.Menu(menu)
file_menu_4 = tk.Menu(menu)
file_menu_5 = tk.Menu(menu)
file_menu_6 = tk.Menu(menu)
file_menu_7 = tk.Menu(menu)
file_menu_8 = tk.Menu(menu)

example_1 = menu.add_cascade(label="File", menu=file_menu_1)
file_menu_1.add_command(label="new file")

example_2 = menu.add_cascade(label="Edit", menu=file_menu_2)
file_menu_2.add_command(label="Undo")

example_3 = menu.add_cascade(label="Selection", menu=file_menu_3)
file_menu_3.add_command(label="select all")

example_4 = menu.add_cascade(label="View", menu=file_menu_4)
file_menu_4.add_command(label="search")

example_5 = menu.add_cascade(label="Go", menu=file_menu_5)
file_menu_5.add_command(label="back")

example_6 = menu.add_cascade(label="Debag", menu=file_menu_6)
file_menu_6.add_command(label="start debugging")

example_7 = menu.add_cascade(label="Termina", menu=file_menu_7)
file_menu_7.add_command(label="new termina")

example_8 = menu.add_cascade(label="Help", menu=file_menu_8)
file_menu_8.add_command(label="welcome")

screen.mainloop()
