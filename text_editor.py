import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser

screen = tk.Tk()
screen.geometry("450x620")
screen_title = "text editor"
screen.title(screen_title)
filename = ""
saved_words = ("import", "from", "as", "def", "class", "if", "elif",
               "else", "while", "for", "do", "print", "int", "float", "str")

Lines_Label_Text = tk.StringVar()

text = tk.Text(screen, undo=True, fg="black")
scroll = tk.Scrollbar(screen, command=text.yview)
Lines_Label = tk.Label(
    screen, text="hi", textvariable=Lines_Label_Text, anchor="sw")
text.configure(yscrollcommand=scroll.set)
text.config(font=("arial", 16, "normal"), fg="black")
scroll.pack(side=tk.RIGHT, fill=tk.Y)
Lines_Label.pack(side=tk.BOTTOM, fill=tk.BOTH)
text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


def update_Lines_Label(c):
    global Lines_Label_Text
    Lines_Label_Text.set(
        "Lines:" + str(int(text.index('end').split('.')[0]) - 1))


def mark_save_words(word):
    text.tag_config("orange_tag", foreground="orange")
    offset = "+%dc" % len(word)
    pos_start = text.search(word, "1.0", tk.END)
    while pos_start:
        pos_end = pos_start + offset
        text.tag_add("orange_tag", pos_start, pos_end)
        pos_start = text.search(word, pos_end, tk.END)


def change_title(c):
    global filename
    global screen_title
    global Lines_Label_Text

    if "Changed" in Lines_Label_Text.get():
        pass
    else:
        Lines_Label_Text.set(Lines_Label_Text.get() + " Changed")

    if filename != "":
        screen.title("*" + filename + " - " + "text editor")
    text.tag_remove("found", "1.0", tk.END)

    for i in saved_words:
        mark_save_words(i)


def change_tab_size(c):
    text.insert(tk.INSERT, " " * 4)
    return "break"


def new_file():
    global text
    global filename
    text.delete(1.0, tk.END)
    newfilename = filedialog.asksaveasfilename(
        filetypes=[("All Files", "*.*"),
                   ("Text Files", "*.txt")]
    )
    if not "." in newfilename:
        newfilename = newfilename + ".txt"
    open(newfilename, "w")
    filename = newfilename
    screen_title = newfilename + " - " + "text editor"
    screen.title(screen_title)


def open_file():
    global filename
    filename = filedialog.askopenfilename(
        filetypes=[("All Files", "*.*"),
                   ("Text Files", "*.txt")]
    )
    text.delete(1.0, tk.END)
    try:
        text.insert(1.0, open(filename, "r").read())
    except:
        pass
    screen_title = filename + " - " + "text editor"
    screen.title(screen_title)


def save_file():
    global filename
    global text
    global Lines_Label_Text
    with open(filename, "w") as f:
        f.write(text.get(1.0, tk.END))
    screen.title(filename + " - " + "text editor")
    Lines_Label_Text.set(
        "Lines:" + str(int(text.index('end').split('.')[0]) - 1))


def cut_text():
    global text
    marked_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    text.delete(tk.SEL_FIRST, tk.SEL_LAST)
    screen.clipboard_clear()
    screen.clipboard_append(marked_text)


def copy_text():
    marked_text = text.get(tk.SEL_FIRST, tk.SEL_LAST)
    screen.clipboard_clear()
    screen.clipboard_append(marked_text)


def paste_text():
    text.insert(tk.END, screen.clipboard_get())


def find_text(s):
    if s:
        idx = "1.0"
        while 1:
            idx = text.search(s, idx, nocase=1, stopindex=tk.END)
            if not idx:
                break
            lastidx = "%s+%dc" % (idx, len(s))
            text.tag_add("found", idx, lastidx)
            idx = lastidx
        text.tag_config("found", background="yellow")


def _find_text():
    find_text_menu = tk.Toplevel()
    s = tk.StringVar()
    text_to_found = tk.Entry(find_text_menu, textvariable=s)
    text_to_found.pack()
    f_button = tk.Button(find_text_menu, text="Find",
                         command=lambda: find_text(s.get()))
    f_button.pack()
    find_text_menu.mainloop()


def replace_text(v1, v2):
    Text_get = text.get("1.0", tk.END)
    text.delete("1.0", "end")
    text.insert("1.0", Text_get.replace(v1, v2))


def _replace_text():
    replace_text_menu = tk.Toplevel()
    v1 = tk.StringVar()
    v2 = tk.StringVar()
    tk.Label(replace_text_menu, text="Find:").pack()
    text_to_found2 = tk.Entry(replace_text_menu, textvariable=v1)
    text_to_found2.pack()
    tk.Label(replace_text_menu, text="Replace With:").pack()
    text_to_replace = tk.Entry(replace_text_menu, textvariable=v2)
    text_to_replace.pack()
    f_button = tk.Button(replace_text_menu, text="Replace",
                         command=lambda: replace_text(v1.get(), v2.get()))
    f_button.pack()
    replace_text_menu.mainloop()


def change_font_settings(F="arial", S=16):
    text.config(font=(F, S))


def font_settings():
    font_settings_menu = tk.Toplevel()
    font_settings_menu.title("font settings")
    font = tk.StringVar()
    size = tk.IntVar()
    label1 = tk.Label(font_settings_menu, text="Font: ")
    label1.grid(row=0, column=0)
    entry1 = tk.Entry(font_settings_menu, textvariable=font)
    entry1.grid(row=0, column=1)
    label2 = tk.Label(font_settings_menu, text="Size : ")
    label2.grid(row=1, column=0)
    entry2 = tk.Entry(font_settings_menu, textvariable=size)
    entry2.grid(row=1, column=1)
    submit_button = tk.Button(font_settings_menu, text="Submit",
                              command=lambda: change_font_settings(F=font.get(), S=entry2.get()))
    submit_button.grid(row=2, column=0)
    submit_button.config(height=2, width=6)
    font_settings_menu.mainloop()


def color_settings():
    color_settings_menu = tk.Toplevel()
    color_settings_menu.title("font settings")
    label3 = tk.Label(color_settings_menu, text="BackGround color: ")
    label3.grid(row=0, column=0)
    Button1 = tk.Button(color_settings_menu, text="Pick Color", command=lambda: text.config(
        bg=colorchooser.askcolor()[1]))
    Button1.grid(row=0, column=1)
    label4 = tk.Label(color_settings_menu, text="Font color: ")
    label4.grid(row=1, column=0)
    Button2 = tk.Button(color_settings_menu, text="Pick Color", command=lambda: text.config(
        fg=colorchooser.askcolor()[1]))
    Button2.grid(row=1, column=1)
    color_settings_menu.mainloop()


def complete(c):
    if c == "(":
        offset = "+%dc" % (len(c))
        pos_start = text.search(c, "1.0", tk.END)
        if pos_start == "":
            pos_end = "1.0" + offset
        else:
            pos_end = pos_start + offset
        text.insert(pos_end, " )")
    elif c == "[":
        offset = "+%dc" % (len(c))
        pos_start = text.search(c, "1.0", tk.END)
        if pos_start == "":
            pos_end = "1.0" + offset
        else:
            pos_end = pos_start + offset
        text.insert(pos_end, " ]")
    elif c == "{":
        offset = "+%dc" % (len(c))
        pos_start = text.search(c, "1.0", tk.END)
        if pos_start == "":
            pos_end = "1.0" + offset
        else:
            pos_end = pos_start + offset
        text.insert(pos_end, "\n}")
    elif c == '"':
        offset = "+%dc" % (len(c) + 2)
        pos_start = text.search(c, "1.0", tk.END)
        if pos_start == "":
            pos_end = "2.0" + offset
        else:
            pos_end = pos_start + offset
        text.insert(pos_end, '"')
    elif c == "'":
        offset = "+%dc" % (len(c) + 2)
        pos_start = text.search(c, "1.0", tk.END)
        if pos_start == "":
            pos_end = "2.0" + offset
        else:
            pos_end = pos_start + offset
        text.insert(pos_end, "'")


menubar = tk.Menu(screen)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="New File", accelerator="Ctrl+N", command=new_file)
filemenu.add_separator()
filemenu.add_command(label="Open", accelerator="Ctrl+O", command=open_file)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=save_file)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=screen.quit)
menubar.add_cascade(label="File",  menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=cut_text)
editmenu.add_command(label="Copy", accelerator="Ctrl+V", command=copy_text)
editmenu.add_command(label="Paste", accelerator="Ctrl+C", command=paste_text)
editmenu.add_command(label="Undo", accelerator="Ctrl+Z",
                     command=text.edit_undo)
editmenu.add_command(label="Redo", accelerator="Ctrl+Y",
                     command=text.edit_redo)
editmenu.add_separator()
editmenu.add_command(label="Find", accelerator="Ctrl+F", command=_find_text)
editmenu.add_command(label="Replace", accelerator="Ctrl+H",
                     command=_replace_text)
menubar.add_cascade(label="Edit", menu=editmenu)

settingsmenu = tk.Menu(menubar, tearoff=0)
settingsmenu.add_command(label="Font", command=font_settings)
settingsmenu.add_command(label="Color", command=color_settings)
menubar.add_cascade(label="Settings", menu=settingsmenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label="About")
menubar.add_cascade(label="Help", menu=helpmenu)

screen.bind("<KeyPress>", change_title)
text.bind("<Tab>", change_tab_size)
screen.bind("(", lambda x: complete("("))
screen.bind("[", lambda x: complete("["))
screen.bind("{", lambda x: complete("{"))
text.bind('"', lambda x: complete('"'))
text.bind("'", lambda x: complete("'"))
text.bind("<Button-1>", update_Lines_Label)
# regular bind
screen.bind("<Control-n>", lambda x: new_file())
screen.bind("<Control-o>", lambda x: open_file())
screen.bind("<Control-s>", lambda x: save_file())
screen.bind("<Control-x>", lambda x: cut_text())
screen.bind("<Control-c>", lambda x: copy_text())
screen.bind("<Control-v>", lambda x: paste_text())
screen.bind("<Control-z>", lambda x: text.edit_undo())
screen.bind("<Control-y>", lambda x: text.edit_redo())
# upper bind
screen.bind("<Control-N>", lambda x: new_file())
screen.bind("<Control-O>", lambda x: open_file())
screen.bind("<Control-S>", lambda x: save_file())
screen.bind("<Control-X>", lambda x: cut_text())
screen.bind("<Control-C>", lambda x: copy_text())
screen.bind("<Control-V>", lambda x: paste_text())
screen.bind("<Control-Z>", lambda x: text.edit_undo())
screen.bind("<Control-Y>", lambda x: text.edit_redo())
screen.config(menu=menubar)
screen.mainloop()

