from ttkbootstrap import Style 
from tkinter import ttk 

style = Style('cyborg')
window = style.master 

b1 = ttk.Button(window, text="Submit", style='primary.TButton')
b1.pack(side='left', padx=5, pady=10) 
b2 = ttk.Button(window, text="Submit", style='primary.Outline.TButton')
b2.pack(side='left', padx=5, pady=10)
pb1 = ttk.Progressbar(window, style='danger.Striped.Horizontal.TProgressbar')
pb1.pack()

window.mainloop() 
