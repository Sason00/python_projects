import requests
import tkinter as tk 
from tkinter import ttk
from bs4 import BeautifulSoup

screen = tk.Tk()
pokemon = tk.StringVar()
entry1 = ttk.Entry(screen)
submit = ttk.Button(screen)
pokemon_list_box = tk.Listbox(screen)
label_types = tk.Label(screen)
label_offence = tk.Label(screen)
label_deffence = tk.Label(screen)
label_uneffective = tk.Label(screen)
label_effective = tk.Label(screen)
error_label = tk.Label(screen)
return_button = ttk.Button(screen)
purl = requests.get("https://rankedboost.com/pokemon-go/pokedex/")
psoup = BeautifulSoup(purl.text, "html.parser")
pokemons = []
for i in psoup.findAll("span", {"class":"PokemonName"}):
    pokemons.append(i.text)
 
def get_type(type_div):
    return_list = []
    for i in type_div.findAll("div", {"class":"large-type"})[0].findAll("div", {"class":"type"}):
        return_list.append(i.text)
    return return_list

def get_offense_moveset(table1):
    return (table1.findAll("a")[0].text, table1.findAll("td")[1].text, table1.findAll("a")[1].text, table1.findAll("td")[3].text)


def get_deffense_moveset(table2):
    return (table2.findAll("a")[0].text, table2.findAll("td")[1].text, table2.findAll("a")[1].text, table2.findAll("td")[3].text)


def get_uneffective(type_div):
    return_list = []
    for i in type_div.find("div").findAll("div", {"class":"grid"})[0].find("div").findAll("a", {"class":"type"}):
        return_list.append(i.text)
    return return_list


def get_effective(type_div):
    return_list = []
    for i in type_div.findAll("div")[-1].findAll("a", {"class":"type"}):
        return_list.append(i.text)
    return return_list


def show_stats(p):
    global label_types
    global label_offence 
    global label_deffence 
    global label_uneffective 
    global label_effective 
    global return_button
    global error_label
    entry1.destroy()
    submit.destroy()
    pokemon_list_box.destroy()
    url = requests.get("https://pokemon.gameinfo.io/en/pokemon/" + p)
    soup = BeautifulSoup(url.text, "html.parser")
    if soup.title.text == "Pokémon GO - 404":
        label_text = "pokemon not found"
        error_label = tk.Label(screen, text=label_text)
        error_label.grid(row=0, column=0)
    else:        
        table1 = soup.findAll("table", {"class":"moveset"})[0]
        table2 = soup.findAll("table", {"class":"moveset"})[1]
        type_div = soup.find("article", {"class":"pokemon-type"})
        label_text = "type:\n"
        for i in get_type(type_div):
            label_text = label_text + i + "\n"
        label_types = tk.Label(screen, text=label_text)
        label_types.grid(row=0, column=0)
        label_text = "offense_moveset:\n"
        for i in get_offense_moveset(table1):
            label_text = label_text + i + "\n"
        label_offence = tk.Label(screen, text=label_text)
        label_offence.grid(row=0, column=1)
        label_text ="deffens:\n"
        for i in get_deffense_moveset(table2):
            label_text = label_text + i + "\n"
        label_deffence = tk.Label(screen, text=label_text)
        label_deffence.grid(row=0, column=2)
        label_text =  "uneffective:\n"
        for i in get_uneffective(type_div):
            label_text = label_text + i + "\n"
        label_uneffective = tk.Label(screen, text=label_text)
        label_uneffective.grid(row=0, column=3)
        label_text =  "effective:\n"
        for i in get_effective(type_div):
            label_text = label_text + i + "\n"
        label_effective = tk.Label(screen, text=label_text)
        label_effective.grid(row=0, column=4)
    return_button = ttk.Button(screen, text="return", command=main)
    return_button.grid(row=1, column=0)




def main():
    global entry1
    global submit
    global pokemon_list_box
    label_types.destroy()
    label_offence.destroy()
    label_deffence.destroy() 
    label_uneffective.destroy() 
    label_effective.destroy() 
    error_label.destroy()
    return_button.destroy()
    return_button.destroy()
    entry1 = ttk.Entry(screen, textvariable=pokemon)
    entry1.grid(row=0, column=0)
    submit = ttk.Button(screen, text="submit", command=lambda: show_stats(pokemon.get()))
    submit.grid(row=0, column=1)
    pokemon_list_box = tk.Listbox(screen)
    pokemon_list_box.grid(row=1, column=0)
    for i in pokemons:
        pokemon_list_box.insert(tk.END, i)

if __name__ == "__main__":
    main()

screen.mainloop()