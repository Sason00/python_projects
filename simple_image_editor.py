import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from PIL import ImageTk

screen = tk.Tk()
global file_dir

menubar = tk.Menu(screen)

def change_file_dir():
    file_dir = askopenfilename()

def ask_file_dir():
    ask_file_menu = tk.Toplevel()
    pick_file = tk.Button(ask_file_dir, text="pick image", command=change_file_dir)
    pick_file.pack()
    ask_file_menu.mainloop()

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New File", command=ask_file_dir)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=screen.quit)
menubar.add_cascade(label="File", menu=file_menu)

screen.config(menu=menubar)
screen.mainloop()