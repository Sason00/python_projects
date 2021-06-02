import requests
import tkinter as tk 
from tkinter import ttk
from bs4 import BeautifulSoup

screen = tk.Tk()
country = tk.StringVar()
entry1 = ttk.Entry(screen)
submit = ttk.Button(screen)
country_list = tk.Listbox(screen)
text = tk.Label(screen)
return_button = ttk.Button(screen)

countries_url = requests.get("https://www.worldometers.info/coronavirus/")
countries_soup = BeautifulSoup(countries_url.text, "html.parser")
countries = []
for i in countries_soup.findAll("a", {"class": "mt_a"}):
    countries.append(str(i.text))
countries[0] = "us"

def info(country):
    url = requests.get("https://www.worldometers.info/coronavirus/country/" + country)
    soup = BeautifulSoup(url.text, "html.parser")
    items = []
    isok = False
    isok = isok
    if soup.title.text == "404 Not Found":
        return 
    for i in soup.find_all(id="maincounter-wrap"):
        if str(i) == "Projections":
            break
        for j in str(i.text):
            if str(j).islower():
                isok = True
                items.append(str(i.text).replace("\n", ""))
                break
        isok = False
    t = 0
    for i in items:
        items[t] = i.split(":")
        t += 1
    return items





def text_window(c):
    global entry1
    global submit
    global text
    global return_button
    global country_list
    info_list = info(c)
    entry1.destroy()
    submit.destroy()
    country_list.destroy()
    text_to_write = c + "\n"
    if info_list == None:
        text = tk.Label(screen, text="country dont exist")
        text.grid(row=0, column=0)
    else:
        for i in info_list:
            for j in range(len(i)):
                text_to_write = text_to_write + i[j]
                if j == 0:
                    text_to_write = text_to_write + ": "
            text_to_write = text_to_write + "\n"
        text = tk.Label(screen, text=text_to_write)
        text.grid(row=0, column=0)
    return_button = ttk.Button(screen, text="return", command=main)
    return_button.grid(row=1, column=0)

def main():
    global entry1
    global submit
    global text
    global return_button
    global country_list
    text.destroy()
    return_button.destroy()
    country = tk.StringVar()
    entry1 = ttk.Entry(screen, textvariable=country)
    entry1.grid(row=0, column=0)
    submit = ttk.Button(screen, text="submit", command=lambda:text_window(country.get()))
    submit.grid(row=0, column=1)
    country_list = tk.Listbox(screen)
    country_list.grid(row=1, column=0)
    for i in countries:
        country_list.insert(tk.END, i)
if __name__ == "__main__":
    main()

screen.mainloop()