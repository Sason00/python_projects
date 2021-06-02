import tkinter as tk
from tkinter import ttk, colorchooser
import time

screen = tk.Tk()

editroot = tk.Frame(screen, width=500, height=500,
                    borderwidth=1, relief="solid")
editroot.grid(row=0, column=0)

buttons = []
labels = []
entrys = []
radiobuttons = []
spinboxes = []
texts = []
scales = []
listboxes = []
optionmenus = []
images = []
labelImages = []
ttk_buttons_frames = []
ttk_buttons = []
ttk_entrys_frames = []
ttk_entrys = []
ttk_radiobuttons_frames = []
ttk_radiobuttons = []
ttk_comboboxes_frames = []
ttk_comboboxes = []
ttk_spinboxes_frames = []
ttk_spinboxes = []
ttk_progressbars = []
ttk_scales = []

toolroot = tk.Frame(screen)
toolroot.grid(row=0, column=1)


class TopLevel:
    def resize(self, w):
        self.s = tk.Toplevel(screen)
        self.s.attributes("-toolwindow", True)
        self.s.geometry(str(w.winfo_width()) + "x" + str(w.winfo_height()))
        self.f = tk.Frame(self.s, borderwidth=1, relief="solid")
        self.f.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.r = None
        if type(w) == type(tk.Button()):
            widget = tk.Button(self.f, text=w.cget(
                "text"), width=editroot["width"], height=editroot["height"], compound="c")
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(tk.Entry()):
            widget = tk.Entry(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(tk.Spinbox()):
            widget = tk.Spinbox(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(tk.Text()):
            widget = tk.Text(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(tk.Scale()):
            widget = tk.Scale(
                self.f, width=editroot["width"], orient=w.cget("orient"))
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(tk.Listbox()):
            widget = tk.Listbox(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
            for i in w.list:
                widget.insert(tk.END, i)
        elif type(w) == type(ttk.Button()):
            widget = ttk.Button(self.f, text=w.cget(
                "text"), width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(ttk.Entry()):
            widget = ttk.Entry(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(ttk.Combobox()):
            widget = ttk.Combobox(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(ttk.Spinbox()):
            widget = ttk.Spinbox(self.f, width=editroot["width"])
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(ttk.Progressbar()):
            widget = ttk.Progressbar(self.f, orient=w.cget("orient"))
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        elif type(w) == type(ttk.Scale()):
            widget = ttk.Scale(self.f, orient=w.cget("orient"))
            widget.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.s.bind("<Return>", lambda x: self.return_value(
            (self.f.winfo_width(), self.f.winfo_height())))
        while self.r is None:
            time.sleep(0.01)
            screen.update()

    def change_font(self, w):
        self.s = tk.Toplevel()
        self.s.attributes("-toolwindow", True)
        self.fonts = ["Arial", "Times", "Helvetica", "Symbol"]
        self.r = None
        self.f = tk.Frame(self.s)
        self.f.pack()
        self.combobox = ttk.Combobox(self.f, values=self.fonts)
        self.combobox.grid(row=0, column=0)
        self.b = ttk.Button(self.f, text="apply", command=lambda: self.label.config(
            font=(self.combobox.get(), 14)))
        self.b.grid(row=0, column=1)
        self.label = tk.Label(self.s)
        if type(w) == type(tk.Label()):
            self.label.configure(text=w.cget("text"))
        else:
            self.label.configure(text="example")
        self.label.pack()
        self.combobox.bind("<<ComboboxSelected>>", lambda x: self.label.config(
            font=(self.combobox.get(), w.cget("font").split(" ")[1])))
        self.submit = ttk.Button(
            self.s, text="Submit", command=lambda: self.return_value(self.combobox.get()))
        self.submit.pack()
        self.s.bind("<Return>", lambda x: self.return_value(
            self.combobox.get()))
        while self.r is None:
            time.sleep(0.01)
            screen.update()

    def change_orient(self, w):
        self.s = tk.Toplevel()
        self.s.attributes("-toolwindow", True)
        self.r = None
        self.f = tk.Frame(self.s)
        self.f.pack()
        self.combobox = ttk.Combobox(
            self.f, values=[tk.HORIZONTAL, tk.VERTICAL])
        self.combobox.current(0)
        self.combobox.grid(row=0, column=0)
        self.progressbar = ttk.Progressbar(self.s)
        self.progressbar.pack()
        self.combobox.bind("<<ComboboxSelected>>", lambda x: self.progressbar.config(
            orient=self.combobox.get()))
        self.submit = ttk.Button(
            self.s, text="Submit", command=lambda: self.return_value(self.combobox.get()))
        self.submit.pack()
        self.s.bind("<Return>", lambda x: self.return_value(
            self.combobox.get()))
        while self.r is None:
            time.sleep(0.01)
            screen.update()

    def resize_screen(self, w):
        self.s = tk.Toplevel()
        self.s.attributes("-toolwindow", True)
        self.s.geometry(str(w.winfo_width()) + "x" + str(w.winfo_height()))
        self.f = tk.Frame(self.s, borderwidth=1, relief="solid")
        self.f.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
        self.r = None
        self.s.bind("<Return>", lambda x: self.return_value(
            (self.f.winfo_width(), self.f.winfo_height())))
        while self.r is None:
            time.sleep(0.01)
            screen.update()

    def askinteger(self, title="", prompt=""):
        self.s = tk.Toplevel()
        self.s.attributes("-toolwindow", True)
        self.r = None
        self.s.title(title)
        self.f = tk.Frame(self.s)
        self.f.grid(row=0, column=0, columnspan=2)
        self.l = ttk.Label(self.f, text=prompt)
        self.l.pack()
        self.v = tk.IntVar()
        self.e = ttk.Entry(self.f, textvariable=self.v)
        self.e.pack()
        self.e.focus()
        self.ok = ttk.Button(
            self.s, text="ok", command=lambda: self.return_value(self.e.get()))
        self.ok.grid(row=1, column=0)
        self.cancel = ttk.Button(
            self.s, text="cancel", command=lambda: self.s.destroy())
        self.cancel.grid(row=1, column=1)
        self.s.bind("<Return>", lambda x: self.return_value(self.e.get()))
        while self.r is None:
            time.sleep(0.01)
            screen.update()

    def askstring(self, title="", prompt=""):
        self.s = tk.Toplevel()
        self.s.attributes("-toolwindow", True)
        self.s.focus()
        self.r = None
        self.s.title(title)
        self.f = tk.Frame(self.s)
        self.f.grid(row=0, column=0, columnspan=2)
        self.l = ttk.Label(self.f, text=prompt)
        self.l.pack()
        self.v = tk.StringVar()
        self.e = ttk.Entry(self.f, textvariable=self.v)
        self.e.pack()
        self.ok = ttk.Button(
            self.s, text="ok", command=lambda: self.return_value(self.e.get()))
        self.ok.grid(row=1, column=0)
        self.cancel = ttk.Button(
            self.s, text="cancel", command=lambda: self.s.destroy())
        self.cancel.grid(row=1, column=1)
        self.s.bind("<Return>", lambda x: self.return_value(self.e.get()))
        while self.r is None:
            time.sleep(0.01)
            screen.update()

    def return_value(self, args):
        self.r = args
        self.s.destroy()


def rename_widget(w):
    askname = TopLevel()
    askname.askstring(title="add text", prompt="add text:")
    w.config(text=askname.r)


def resize_widget(w):
    resizeroot = TopLevel()
    resizeroot.resize(w)
    if type(w) == type(tk.Button()):
        w.place(x=w.winfo_x() - 1, y=w.winfo_y() - 1,
                width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(tk.Entry()):
        w.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(tk.Spinbox()):
        w.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(tk.Text()):
        w.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(tk.Scale()):
        w.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(tk.Listbox()):
        w.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(ttk.Button()):
        w.packed.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(ttk.Entry()):
        w.packed.place(width=resizeroot.r[0], height=resizeroot.r[1])
    elif type(w) == type(ttk.Combobox()):
        w.packed.place(width=resizeroot.r[0])
    elif type(w) == type(ttk.Spinbox()):
        w.packed.place(width=resizeroot.r[0])
    elif type(w) == type(ttk.Progressbar()):
        if str(w.cget("orient")) == str(tk.HORIZONTAL):
            w.configure(length=resizeroot.r[0])
        elif str(w.cget("orient")) == str(tk.VERTICAL):
            w.configure(length=resizeroot.r[1])
    elif type(w) == type(ttk.Scale()):
        w.place(width=resizeroot.r[0], height=resizeroot.r[1])


def change_font(w):
    if type(w) == type(tk.Label()):
        changefontroot = TopLevel(screen)
        changefontroot.change_font(w)
        w.config(font=(changefontroot.r, w.cget("font").split(" ")[1]))
    elif type(w) == type(tk.Radiobutton()):
        changefontroot = TopLevel(screen)
        changefontroot.change_font(w)
        w.config(font=(changefontroot.r, w.cget("font").split(" ")[1]))
    elif type(w) == type(tk.Text()):
        changefontroot = TopLevel(screen)
        changefontroot.change_font(w)
        w.config(font=(changefontroot.r, 14))
    elif type(w) == type(tk.Listbox()):
        changefontroot = TopLevel(screen)
        changefontroot.change_font(w)
        w.config(font=(changefontroot.r, 14))


def change_font_size(w):
    askname = TopLevel(screen)
    askname.askinteger(title="Font Size", prompt="Font Size")
    w.config(font=("Arial", askname.r))


def change_bg(w):
    w.config(bg=colorchooser.askcolor()[1])


def change_abg(w):
    w.config(activebackground=colorchooser.askcolor()[1])


def change_fg(w):
    w.config(fg=colorchooser.askcolor()[1])


def change_afg(w):
    w.config(activeforeground=colorchooser.askcolor()[1])


def change_bw(w):
    askname = TopLevel()
    askname.askstring(title="enter number", prompt="enter border width")
    w.config(borderwidth=askname.r)


def change_orient(w):
    choose_orient = TopLevel()
    choose_orient.change_orient(w)
    w.config(orient=choose_orient.r)


def add_list(w):
    askname = TopLevel()
    askname.askstring(title="enter list", prompt="enter list")
    myList = []
    exec("myList += " + askname.r)
    if type(w) == type(tk.Listbox()):
        for i in range(len(myList)):
            w.insert(tk.END, str(myList[i]))
            w.list += str(myList[i])
    elif type(w) == type(ttk.Combobox()):
        w.list = myList
        w.config(values=myList)


def resize_screen(w):
    resizeroot = TopLevel()
    resizeroot.resize_screen(w)
    w, h = resizeroot.r
    editroot.config(width=w, height=h)


def delete(w):
    w.destroy()
    if type(w) == type(tk.Button()):
        buttons.remove(w)
    elif type(w) == type(tk.Label()):
        labels.remove(w)
    elif type(w) == type(tk.Entry()):
        entrys.remove(w)
    elif type(w) == type(tk.Radiobutton()):
        radiobuttons.remove(w)
    elif type(w) == type(tk.Spinbox()):
        spinboxes.remove(w)
    elif type(w) == type(tk.Text()):
        texts.remove(w)
    elif type(w) == type(tk.Scale()):
        scales.remove(w)
    elif type(w) == type(tk.Listbox()):
        listboxes.remove(w)
    elif type(w) == type(tk.Listbox()):
        optionmenus.remove(w)
    elif type(w) == type(ttk.Label()):
        index = labelImages.index(w)
        images.remove(images[index])
        labelImages.remove(w)
    elif type(w) == type(ttk.Button()):
        index = ttk_buttons.index(w)
        ttk_buttons_frames.remove(ttk_buttons_frames[index])
        ttk_buttons.remove(w)
    elif type(w) == type(ttk.Entry()):
        index = ttk_entrys.index(w)
        ttk_entrys_frames.remove(ttk_entrys_frames[index])
        ttk_entrys.remove(w)
    elif type(w) == type(ttk.Radiobutton()):
        index = ttk_radiobuttons.index(w)
        ttk_radiobuttons_frames.remove(ttk_radiobuttons_frames[index])
        ttk_radiobuttons.remove(w)
    elif type(w) == type(ttk.Combobox()):
        index = ttk_comboboxes.index(w)
        ttk_comboboxes_frames.remove(ttk_comboboxes_frames[index])
        ttk_comboboxes.remove(w)
    elif type(w) == type(ttk.Spinbox()):
        index = ttk_spinboxes.index(w)
        ttk_spinboxes_frames.remove(ttk_spinboxes_frames[index])
        ttk_spinboxes.remove(w)
    elif type(w) == type(ttk.Progressbar()):
        ttk_progressbars.remove(w)


def left_click_popup(e):
    m = tk.Menu(screen, tearoff=0)
    if type(e.widget) == type(tk.Label()):
        m.add_command(label="Rename", command=lambda: rename_widget(e.widget))
        m.add_command(label="Font size",
                      command=lambda: change_font_size(e.widget))
        stylemenu = tk.Menu(m, tearoff=0)
        stylemenu.add_command(label="Change Font",
                              command=lambda: change_font(e.widget))
        stylemenu.add_command(label="Change Background Color",
                              command=lambda: change_bg(e.widget))
        stylemenu.add_command(label="Change Font Color",
                              command=lambda: change_fg(e.widget))
        m.add_cascade(label="Style Option", menu=stylemenu)
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Button()):
        m.add_command(label="Rename", command=lambda: rename_widget(e.widget))
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        stylemenu = tk.Menu(m, tearoff=0)
        stylemenu.add_command(label="Change Background Color",
                              command=lambda: change_bg(e.widget))
        stylemenu.add_command(label="Change Font Color",
                              command=lambda: change_fg(e.widget))
        stylemenu.add_command(
            label="Change Active Background Color", command=lambda: change_abg(e.widget))
        stylemenu.add_command(label="Change Active Font Color",
                              command=lambda: change_afg(e.widget))
        stylemenu.add_command(label="Change Border Width",
                              command=lambda: change_bw(e.widget))
        m.add_cascade(label="Style Option", menu=stylemenu)
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Entry()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Radiobutton()):
        m.add_command(label="Rename", command=lambda: rename_widget(e.widget))
        m.add_command(label="Font size",
                      command=lambda: change_font_size(e.widget))
        stylemenu = tk.Menu(m, tearoff=0)
        stylemenu.add_command(label="Change Font",
                              command=lambda: change_font(e.widget))
        stylemenu.add_command(label="Change Background Color",
                              command=lambda: change_bg(e.widget))
        stylemenu.add_command(label="Change Font Color",
                              command=lambda: change_fg(e.widget))
        m.add_cascade(label="Style Option", menu=stylemenu)
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Spinbox()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Text()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_command(label="Font size",
                      command=lambda: change_font_size(e.widget))
        stylemenu = tk.Menu(m, tearoff=0)
        stylemenu.add_command(label="Change Font",
                              command=lambda: change_font(e.widget))
        stylemenu.add_command(label="Change Background Color",
                              command=lambda: change_bg(e.widget))
        stylemenu.add_command(label="Change Font Color",
                              command=lambda: change_fg(e.widget))
        m.add_cascade(label="Style Option", menu=stylemenu)
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Scale()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_command(label="Font size",
                      command=lambda: change_font_size(e.widget))
        m.add_command(label="Orient", command=lambda: change_orient(e.widget))
        stylemenu = tk.Menu(m, tearoff=0)
        stylemenu.add_command(label="Change Background Color",
                              command=lambda: change_bg(e.widget))
        stylemenu.add_command(label="Change Font Color",
                              command=lambda: change_fg(e.widget))
        m.add_cascade(label="Style Option", menu=stylemenu)
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Listbox()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_command(label="Add List", command=lambda: add_list(e.widget))
        stylemenu = tk.Menu(m, tearoff=0)
        stylemenu.add_command(label="Change Font",
                              command=lambda: change_font(e.widget))
        stylemenu.add_command(label="Change Background Color",
                              command=lambda: change_bg(e.widget))
        stylemenu.add_command(label="Change Font Color",
                              command=lambda: change_fg(e.widget))
        m.add_cascade(label="Style Option", menu=stylemenu)
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.OptionMenu(screen, None, None)):
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Button()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Entry()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Radiobutton()):
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Combobox()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_command(label="Add List", command=lambda: add_list(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Spinbox()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Progressbar()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_command(label="Orient", command=lambda: change_orient(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(ttk.Scale()):
        m.add_command(label="Resize", command=lambda: resize_widget(e.widget))
        m.add_command(label="Orient", command=lambda: change_orient(e.widget))
        m.add_separator()
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    elif type(e.widget) == type(tk.Frame()):
        m.add_command(label="Resize Screen",
                      command=lambda: resize_screen(e.widget))
        m.add_command(label="Change Background Color",
                      command=lambda: change_bg(e.widget))
    elif type(e.widget) == type(ttk.Label()):
        m.add_command(label="Delete", command=lambda: delete(e.widget))
    try:
        m.tk_popup(e.x_root, e.y_root)
    finally:
        m.grab_release()


def start_drag(e):
    if type(e.widget) == type(ttk.Button()):
        w = e.widget.packed
        w._drag_start_x = e.x
        w._drag_start_y = e.y
    elif type(e.widget) == type(ttk.Entry()):
        w = e.widget.packed
        w._drag_start_x = e.x
        w._drag_start_y = e.y
    elif type(e.widget) == type(ttk.Radiobutton()):
        w = e.widget.packed
        w._drag_start_x = e.x
        w._drag_start_y = e.y
    elif type(e.widget) == type(ttk.Combobox()):
        w = e.widget.packed
        w._drag_start_x = e.x
        w._drag_start_y = e.y
    elif type(e.widget) == type(ttk.Spinbox()):
        w = e.widget.packed
        w._drag_start_x = e.x
        w._drag_start_y = e.y
    else:
        w = e.widget
        w._drag_start_x = e.x
        w._drag_start_y = e.y


def drag(e):
    if type(e.widget) == type(ttk.Button()):
        widget = e.widget.packed
        x = widget.winfo_x() - widget._drag_start_x + e.x
        y = widget.winfo_y() - widget._drag_start_y + e.y
        widget.place(x=x, y=y)
    elif type(e.widget) == type(ttk.Entry()):
        widget = e.widget.packed
        x = widget.winfo_x() - widget._drag_start_x + e.x
        y = widget.winfo_y() - widget._drag_start_y + e.y
        widget.place(x=x, y=y)
    elif type(e.widget) == type(ttk.Radiobutton()):
        widget = e.widget.packed
        x = widget.winfo_x() - widget._drag_start_x + e.x
        y = widget.winfo_y() - widget._drag_start_y + e.y
        widget.place(x=x, y=y)
    elif type(e.widget) == type(ttk.Combobox()):
        widget = e.widget.packed
        x = widget.winfo_x() - widget._drag_start_x + e.x
        y = widget.winfo_y() - widget._drag_start_y + e.y
        widget.place(x=x, y=y)
    elif type(e.widget) == type(ttk.Spinbox()):
        widget = e.widget.packed
        x = widget.winfo_x() - widget._drag_start_x + e.x
        y = widget.winfo_y() - widget._drag_start_y + e.y
        widget.place(x=x, y=y)
    else:
        widget = e.widget
        x = widget.winfo_x() - widget._drag_start_x + e.x
        y = widget.winfo_y() - widget._drag_start_y + e.y
        widget.place(x=x, y=y)


def add_button():
    askname = TopLevel()
    askname.askstring(title="add text", prompt="add text:")
    b = tk.Button(editroot, text=askname.r, padx=0, pady=0, compound="c")
    b.place(x=0, y=0, width=50, height=50)
    b.bind("<Button-1>", start_drag)
    b.bind("<B1-Motion>", drag)
    b.bind("<Button-3>", left_click_popup)
    buttons.append(b)


def add_label():
    askname = TopLevel()
    askname.askstring(title="add text", prompt="add text:")
    l = tk.Label(editroot, text=askname.r, font=("arial", 14))
    l.place(x=0, y=0)
    l.bind("<Button-1>", start_drag)
    l.bind("<B1-Motion>", drag)
    l.bind("<Button-3>", left_click_popup)
    labels.append(l)


def add_entry():
    e = tk.Entry(editroot)
    # e.configure(state=tk.DISABLED)
    e.place(x=0, y=0)
    e.bind("<Button-1>", start_drag)
    e.bind("<B1-Motion>", drag)
    e.bind("<Button-3>", left_click_popup)
    entrys.append(e)


def add_radiobutton():
    askname = TopLevel()
    askname.askstring(title="add text", prompt="add text:")
    r = tk.Radiobutton(editroot, text=askname.r, font=("arial", 14))
    r.place(x=0, y=0)
    r.bind("<Button-1>", start_drag)
    r.bind("<B1-Motion>", drag)
    r.bind("<Button-3>", left_click_popup)
    radiobuttons.append(r)


def add_spinbox():
    first = TopLevel()
    first.askinteger(title="enter number", prompt="enter first number")
    last = TopLevel()
    last.askinteger(title="enter number", prompt="enter end number")
    s = tk.Spinbox(editroot, from_=first.r, to=last.r)
    s.place(x=0, y=0)
    s.from_ = first.r
    s.to = last.r
    s.bind("<Button-1>", start_drag)
    s.bind("<B1-Motion>", drag)
    s.bind("<Button-3>", left_click_popup)
    spinboxes.append(s)


def add_text():
    t = tk.Text(editroot, font=("arial", 14), borderwidth=1, relief="groove")
    t.place(x=0, y=0, width=300, height=100)
    t.bind("<Button-1>", start_drag)
    t.bind("<B1-Motion>", drag)
    t.bind("<Button-3>", left_click_popup)
    texts.append(t)


def add_scale():
    first = TopLevel()
    first.askinteger(title="enter number", prompt="enter first number")
    last = TopLevel()
    last.askinteger(title="enter number", prompt="enter end number")
    sc = tk.Scale(editroot, from_=first.r, to=last.r)
    sc.configure(state=tk.DISABLED)
    sc.place(x=0, y=0, width=300, height=100)
    sc.from_ = first.r
    sc.to = last.r
    sc.bind("<Button-1>", start_drag)
    sc.bind("<B1-Motion>", drag)
    sc.unbind("<Button-3>")
    sc.bind("<Button-3>", left_click_popup)
    scales.append(sc)


def add_listbox():
    lb = tk.Listbox(editroot, font=("arial", 14),
                    borderwidth=1, relief="groove")
    lb.place(x=0, y=0)
    lb.list = []
    lb.bind("<Button-1>", start_drag)
    lb.bind("<B1-Motion>", drag)
    lb.bind("<Button-3>", left_click_popup)
    listboxes.append(lb)


def add_optionmenu():
    asklist = TopLevel()
    asklist.askstring(title="enter list", prompt="enter list")
    omList = []
    exec("omList +=" + asklist.r)
    om = tk.OptionMenu(editroot, tk.StringVar(), *omList)
    om.place(x=0, y=0)
    om.list = omList
    om.bind("<Button-1>", start_drag)
    om.bind("<B1-Motion>", drag)
    om.bind("<Button-3>", left_click_popup)
    optionmenus.append(om)


def add_image():
    imagePath = TopLevel()
    imagePath.askstring(title="enter path", prompt="enter path")
    im = tk.PhotoImage(file=imagePath.r)
    li = ttk.Label(editroot, image=im)
    li.image = imagePath.r
    li.place(x=0, y=0)
    li.bind("<Button-1>", start_drag)
    li.bind("<B1-Motion>", drag)
    li.bind("<Button-3>", left_click_popup)
    images.append(im)
    labelImages.append(li)


def add_ttk_button():
    askname = TopLevel()
    askname.askstring(title="add text", prompt="add text:")
    ftb = tk.Frame(editroot)
    tb = ttk.Button(ftb, text=askname.r)
    tb.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
    tb.packed = ftb
    ftb.place(x=0, y=0)
    tb.bind("<Button-1>", start_drag)
    tb.bind("<B1-Motion>", drag)
    tb.bind("<Button-3>", left_click_popup)
    ttk_buttons.append(tb)
    ttk_buttons_frames.append(ftb)


def add_ttk_entry():
    fte = tk.Frame(editroot)
    te = ttk.Entry(fte)
    te.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
    te.packed = fte
    fte.place(x=0, y=0)
    te.bind("<Button-1>", start_drag)
    te.bind("<B1-Motion>", drag)
    te.bind("<Button-3>", left_click_popup)
    ttk_entrys.append(te)
    ttk_entrys_frames.append(fte)


def add_ttk_radiobutton():
    askname = TopLevel()
    askname.askstring(title="add text", prompt="add text:")
    ftr = tk.Frame(editroot)
    tr = ttk.Radiobutton(ftr, text=askname.r)
    tr.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
    tr.packed = ftr
    ftr.place(x=0, y=0)
    tr.bind("<Button-1>", start_drag)
    tr.bind("<B1-Motion>", drag)
    tr.bind("<Button-3>", left_click_popup)
    ttk_radiobuttons.append(tr)
    ttk_radiobuttons_frames.append(ftr)


def add_ttk_combobox():
    ftc = tk.Frame(editroot)
    tc = ttk.Combobox(ftc)
    tc.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
    tc.list = []
    tc.packed = ftc
    ftc.place(x=0, y=0)
    tc.bind("<Button-1>", start_drag)
    tc.bind("<B1-Motion>", drag)
    tc.bind("<Button-3>", left_click_popup)
    ttk_comboboxes.append(tc)
    ttk_comboboxes_frames.append(ftc)


def add_ttk_spinbox():
    first = TopLevel()
    first.askinteger(title="enter number", prompt="enter first number")
    last = TopLevel(screen)
    last.askinteger(title="enter number", prompt="enter end number")
    fts = tk.Frame(editroot)
    ts = ttk.Spinbox(fts, from_=first.r, to=last.r)
    ts.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
    ts.from_ = first.r
    ts.to = last.r
    ts.packed = fts
    fts.place(x=0, y=0)
    ts.bind("<Button-1>", start_drag)
    ts.bind("<B1-Motion>", drag)
    ts.bind("<Button-3>", left_click_popup)
    ttk_spinboxes.append(ts)
    ttk_spinboxes_frames.append(fts)


def add_ttk_progressbar():
    ts = ttk.Progressbar(editroot, orient=tk.HORIZONTAL)
    # print(ts.cget("length"))
    # tk.HORIZONTAL
    # tk.VERTICAL
    # print(type(ts.cget("orient")))
    ts.place(x=0, y=0)
    ts.bind("<Button-1>", start_drag)
    ts.bind("<B1-Motion>", drag)
    ts.bind("<Button-3>", left_click_popup)
    ttk_progressbars.append(ts)


def add_ttk_scale():
    first = TopLevel()
    first.askinteger(title="enter number", prompt="enter first number")
    last = TopLevel(screen)
    last.askinteger(title="enter number", prompt="enter end number")
    tsc = ttk.Scale(editroot, from_=first.r, to=last.r)
    tsc.place(x=0, y=0, width=300, height=100)
    tsc.from_ = first.r
    tsc.to = last.r
    tsc.bind("<Button-1>", start_drag)
    tsc.bind("<B1-Motion>", drag)
    tsc.unbind("<Button-3>")
    tsc.bind("<Button-3>", left_click_popup)
    ttk_scales.append(tsc)


def save():
    code = f"""
import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
screen.geometry("{editroot["width"]}x{editroot["height"]}")
    """

    if editroot.cget("bg") != "systemWindowBody":
        code = code + f"""
screen.config(bg="{editroot.cget("bg")}")
    """

    for i in range(len(buttons)):
        code = code + f"""
myButton{str(i)} = tk.Button(screen, text="{buttons[i].cget("text")}", padx=0, pady=0, bg="{buttons[i].cget("bg")}", fg="{buttons[i].cget("fg")}", activebackground="{buttons[i].cget("activebackground")}", activeforeground="{buttons[i].cget("activeforeground")}", borderwidth={buttons[i].cget("borderwidth")})
myButton{str(i)}.place(x={buttons[i].winfo_x() - 1}, y={buttons[i].winfo_y() - 1}, width={buttons[i].winfo_width()}, height={buttons[i].winfo_height()})
        """

    for i in range(len(labels)):
        code = code + f"""
myLabel{str(i)} = tk.Label(screen, text="{labels[i].cget("text")}", font={labels[i].cget("font").split(" ")}, bg="{labels[i].cget("bg")}", fg="{labels[i].cget("fg")}")
myLabel{str(i)}.place(x={labels[i].winfo_x() - 1}, y={labels[i].winfo_y() - 1})
        """
    for i in range(len(entrys)):
        code = code + f"""
myEntry{str(i)} = tk.Entry(screen)
myEntry{str(i)}.place(x={entrys[i].winfo_x() - 1}, y={entrys[i].winfo_y() - 1}, width={entrys[i].winfo_width()}, height={entrys[i].winfo_height()})
        """

    for i in range(len(spinboxes)):
        code = code + f"""
mySpinbox{str(i)} = tk.Spinbox(screen, from_={spinboxes[i].from_}, to={spinboxes[i].to})
mySpinbox{str(i)}.place(x={spinboxes[i].winfo_x() - 1}, y={spinboxes[i].winfo_y() - 1}, width={spinboxes[i].winfo_width()}, height={spinboxes[i].winfo_height()})
        """

    for i in range(len(radiobuttons)):
        code = code + f"""
myRadioButton{str(i)} = tk.Radiobutton(screen, text="{radiobuttons[i].cget("text")}", font={radiobuttons[i].cget("font").split(" ")}, bg="{radiobuttons[i].cget("bg")}", fg="{radiobuttons[i].cget("fg")}")
myRadioButton{str(i)}.place(x={radiobuttons[i].winfo_x() - 1}, y={radiobuttons[i].winfo_y() - 1})
        """

    for i in range(len(texts)):
        code = code + f"""
myText{str(i)} = tk.Text(screen, bg="{texts[i].cget("bg")}", fg="{texts[i].cget("fg")}", font={texts[i].cget("font").split(" ")})
myText{str(i)}.place(x={texts[i].winfo_x() - 1}, y={texts[i].winfo_y() - 1}, width={texts[i].winfo_width()}, height={texts[i].winfo_height()})
        """

    for i in range(len(scales)):
        code = code + f"""
myScale{str(i)} = tk.Scale(screen, from_={scales[i].from_}, to={scales[i].to}, bg="{scales[i].cget("bg")}", fg="{scales[i].cget("fg")}", orient="{scales[i].cget("orient")}")
myScale{str(i)}.place(x={scales[i].winfo_x() - 1}, y={scales[i].winfo_y() - 1}, width={scales[i].winfo_width()}, height={scales[i].winfo_height()})
        """

    for i in range(len(listboxes)):
        code = code + f"""
myListbox{str(i)} = tk.Listbox(screen, font={listboxes[i].cget("font").split(" ")}, bg="{listboxes[i].cget("bg")}", fg="{listboxes[i].cget("fg")}")
myListbox{str(i)}.place(x={listboxes[i].winfo_x() - 1}, y={listboxes[i].winfo_y() - 1}, width={listboxes[i].winfo_width()}, height={listboxes[i].winfo_height()})
for j in {listboxes[i].list}:
    myListbox{str(i)}.insert(tk.END, j)
        """

    for i in range(len(optionmenus)):
        code = code + f"""
myOptionsMenu{str(i)} = tk.OptionMenu(screen, tk.StringVar(), *{optionmenus[i].list})
myOptionsMenu{str(i)}.place(x={optionmenus[i].winfo_x() - 1}, y={optionmenus[i].winfo_y() - 1})
        """

    for i in range(len(images)):
        code = code + f"""
myImage{str(i)} = tk.PhotoImage(file=r"{labelImages[i].image}")
myLabelImage{str(i)} = tk.Label(screen, image=myImage{str(i)})
myLabelImage{str(i)}.place(x={labelImages[i].winfo_x() - 1}, y={labelImages[i].winfo_y() - 1})
        """

    for i in range(len(ttk_buttons)):
        code = code + f"""
myTtkButtonFrame{str(i)} = tk.Frame(screen)
myTtkButton{str(i)} = ttk.Button(myTtkButtonFrame{str(i)}, text="{ttk_buttons[i].cget("text")}")
myTtkButton{str(i)}.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
myTtkButtonFrame{str(i)}.place(x={ttk_buttons_frames[i].winfo_x() - 1}, y={ttk_buttons_frames[i].winfo_y() - 1}, width={ttk_buttons_frames[i].winfo_width()}, height={ttk_buttons_frames[i].winfo_height()})
        """

    for i in range(len(ttk_entrys)):
        code = code + f"""
myTtkEntryFrame{str(i)} = tk.Frame(screen)
myTtkEntry{str(i)} = ttk.Entry(myTtkEntryFrame{str(i)})
myTtkEntry{str(i)}.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
myTtkEntryFrame{str(i)}.place(x={ttk_entrys_frames[i].winfo_x() - 1}, y={ttk_entrys_frames[i].winfo_y() - 1}, width={ttk_entrys_frames[i].winfo_width()}, height={ttk_entrys_frames[i].winfo_height()})
        """

    for i in range(len(ttk_radiobuttons)):
        code = code + f"""
myTtkRadiobuttonFrame{str(i)} = tk.Frame(screen)
myTtkRadiobutton{str(i)} = ttk.Radiobutton(myTtkRadiobuttonFrame{str(i)}, text="{ttk_radiobuttons[i].cget("text")}")
myTtkRadiobutton{str(i)}.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
myTtkRadiobuttonFrame{str(i)}.place(x={ttk_radiobuttons_frames[i].winfo_x() - 1}, y={ttk_radiobuttons_frames[i].winfo_y() - 1}, width={ttk_radiobuttons_frames[i].winfo_width()}, height={ttk_radiobuttons_frames[i].winfo_height()})
        """

    for i in range(len(ttk_comboboxes)):
        code = code + f"""
myTtkComboboxFrame{str(i)} = tk.Frame(screen)
myTtkCombobox{str(i)} = ttk.Combobox(myTtkComboboxFrame{str(i)}, values={ttk_comboboxes[i].list})
myTtkCombobox{str(i)}.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
myTtkComboboxFrame{str(i)}.place(x={ttk_comboboxes_frames[i].winfo_x() - 1}, y={ttk_comboboxes_frames[i].winfo_y() - 1}, width={ttk_comboboxes_frames[i].winfo_width()})
        """

    for i in range(len(ttk_spinboxes)):
        code = code + f"""
myTtkSpinboxFrame{str(i)} = tk.Frame(screen)
myTtkSpinbox{str(i)} = ttk.Spinbox(myTtkSpinboxFrame{str(i)}, from_={ttk_spinboxes[i].from_}, to={ttk_spinboxes[i].to})
myTtkSpinbox{str(i)}.pack(anchor=tk.N, fill=tk.BOTH, expand=True, side=tk.LEFT)
myTtkSpinboxFrame{str(i)}.place(x={ttk_spinboxes_frames[i].winfo_x() - 1}, y={ttk_spinboxes_frames[i].winfo_y() - 1}, width={ttk_spinboxes_frames[i].winfo_width()})
        """

    for i in range(len(ttk_progressbars)):
        code = code + f"""
myTtkProgressbar{str(i)} = ttk.Progressbar(screen, orient="{ttk_progressbars[i].cget("orient")}", length={ttk_progressbars[i].cget("length")})
myTtkProgressbar{str(i)}.place(x={ttk_progressbars[i].winfo_x() - 1}, y={ttk_progressbars[i].winfo_y() - 1})
        """

    for i in range(len(ttk_scales)):
        code = code + f"""
myTtkScale{str(i)} = ttk.Scale(screen, from_={ttk_scales[i].from_}, to={ttk_scales[i].to}, orient="{ttk_scales[i].cget("orient")}")
myTtkScale{str(i)}.place(x={ttk_scales[i].winfo_x() - 1}, y={ttk_scales[i].winfo_y() - 1}, width={ttk_scales[i].winfo_width()}, height={ttk_scales[i].winfo_height()})
        """

    code = code + "\nscreen.mainloop()"
    print(code)


add_button_to_root = ttk.Button(
    toolroot, text="add button", command=add_button)
add_button_to_root.pack(fill=tk.X, pady=2)
add_label_to_root = ttk.Button(toolroot, text="add label", command=add_label)
add_label_to_root.pack(fill=tk.X, pady=2)
add_entry_to_root = ttk.Button(toolroot, text="add entry", command=add_entry)
add_entry_to_root.pack(fill=tk.X, pady=2)
add_radiobutton_to_root = ttk.Button(
    toolroot, text="add radio button", command=add_radiobutton)
add_radiobutton_to_root.pack(fill=tk.X, pady=2)
add_spinbox_to_root = ttk.Button(
    toolroot, text="add spinbox", command=add_spinbox)
add_spinbox_to_root.pack(fill=tk.X, pady=2)
add_text_to_root = ttk.Button(toolroot, text="add text", command=add_text)
add_text_to_root.pack(fill=tk.X, pady=2)
add_scale_to_root = ttk.Button(toolroot, text="add scale", command=add_scale)
add_scale_to_root.pack(fill=tk.X, pady=2)
add_listbox_to_root = ttk.Button(
    toolroot, text="add listbox", command=add_listbox)
add_listbox_to_root.pack(fill=tk.X, pady=2)
add_optionmenu_to_root = ttk.Button(
    toolroot, text="add option menu", command=add_optionmenu)
add_optionmenu_to_root.pack(fill=tk.X, pady=2)
add_image_to_root = ttk.Button(toolroot, text="add image", command=add_image)
add_image_to_root.pack(fill=tk.X, pady=2)
add_ttk_button_to_root = ttk.Button(
    toolroot, text="add ttk button", command=add_ttk_button)
add_ttk_button_to_root.pack(fill=tk.X, pady=2)
add_ttk_entry_to_root = ttk.Button(
    toolroot, text="add ttk entry", command=add_ttk_entry)
add_ttk_entry_to_root.pack(fill=tk.X, pady=2)
add_ttk_radiobutton_to_root = ttk.Button(
    toolroot, text="add ttk radio button", command=add_ttk_radiobutton)
add_ttk_radiobutton_to_root.pack(fill=tk.X, pady=2)
add_ttk_combobox_to_root = ttk.Button(
    toolroot, text="add ttk combobox", command=add_ttk_combobox)
add_ttk_combobox_to_root.pack(fill=tk.X, pady=2)
add_ttk_spimbox_to_root = ttk.Button(
    toolroot, text="add ttk spinbox", command=add_ttk_spinbox)
add_ttk_spimbox_to_root.pack(fill=tk.X, pady=2)
add_ttk_progressbar_to_root = ttk.Button(
    toolroot, text="add ttk progressbar", command=add_ttk_progressbar)
add_ttk_progressbar_to_root.pack(fill=tk.X, pady=2)
add_ttk_scale_to_root = ttk.Button(
    toolroot, text="add ttk scale", command=add_ttk_scale)
add_ttk_scale_to_root.pack(fill=tk.X, pady=2)


save_button = ttk.Button(toolroot, text="save", command=save)
save_button.pack(fill=tk.X, pady=2)

screen.bind("<Button-3>", left_click_popup)
screen.mainloop()

"""
L = tk.Label(screen, text ="Right-click to display menu", 
          width = 40, height = 20) 
L.pack() 
  
m = tk.Menu(screen, tearoff = 0) 
m.add_command(label ="Cut") 
m.add_command(label ="Copy") 
m.add_command(label ="Paste") 
m.add_command(label ="Reload") 
m.add_separator() 
m.add_command(label ="Rename") 
  
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
L.bind("<Button-3>", do_popup)
"""
