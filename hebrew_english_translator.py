import requests
from bs4 import BeautifulSoup
from string import ascii_letters
import tkinter as tk
from tkinter import ttk

screen = tk.Tk()
entry1 = ttk.Entry(screen)
submit = ttk.Button(screen, text="Submit")
translate_label = tk.Label(screen)
return_button = tk.Button(screen)

def translate(word):
    url = requests.get("https://www.morfix.co.il/" + word)
    soup = BeautifulSoup(url.text, "html.parser")
    translate = soup.findAll("div", {"class":"normal_translation_div"})[0].text.replace("(", "").replace(")", "").replace(";", "").replace("  ", "")
    is_h = True

    if word[0] in ascii_letters:
        is_h = True
    else:
        is_h = False
    if is_h:
        print(1)
        return translate
    else:
        print(2)
        return translate

def translate_page(w):
    global translate_label
    global return_button
    entry1.destroy()
    submit.destroy()
    translate_label = tk.Label(screen, text=w + "\n" + translate(w))
    translate_label.grid(column=0, row=0)
    return_button = ttk.Button(screen, text="return", command=main)
    return_button.grid(column=1, row=0)

def main():
    global entry1
    global submit
    translate_label.destroy()
    word = tk.StringVar()
    entry1 = ttk.Entry(screen, textvariable=word)
    entry1.grid(column=0, row=0)
    submit = ttk.Button(screen, text="Submit", command=lambda:translate_page(word.get()))
    submit.grid(column=1, row=0)

if __name__ == "__main__":
    main()
screen.mainloop()