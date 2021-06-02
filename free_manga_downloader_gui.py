import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import os

screen = tk.Tk()
l1 = tk.Label()
e1 = ttk.Entry()
b1 = ttk.Button()
l2 = tk.Label()
e2 = ttk.Entry()
b2 = ttk.Button()
lb1 = tk.Listbox()
# boruto-naruto-next-generations

def get_manga(manga):
    #manga = input("what manga do you want to download? ")
    url = requests.get("http://www.mangareader.net/" + manga)
    soup = BeautifulSoup(url.text, "html.parser")

    table = soup.find("table", {"class":"d48"})
    chapters = []
    g = 0
    for i in table.find_all("td"): 
        if g % 2 == 0:
            print((g // 2) - 1)
            print(i.text)
            chapters.append(i.text)
        g += 1

    g //= 2
    print(g - 1)
    return chapters

def get_chapter_url(manga, chapter):
    #chapter = input("what chapter do you wont to download(number)? ")
    url = requests.get("http://www.mangareader.net/" + manga + "/" + chapter)
    soup = BeautifulSoup(url.text, "html.parser")

    pages = requests.get("http://www.mangareader.net/" + manga + "/" + chapter + "/999999999")
    pages = int(str(pages.url).split("/")[-1])
    urls = []

    for i in range(1, pages + 1):
        url = requests.get("http://www.mangareader.net/" + manga + "/" + chapter + "/" + str(i))
        soup = BeautifulSoup(url.text, "html.parser")
        urls.append("http:" + soup.find("img", {"id":"ci"})["src"])
    return (urls, pages)

def make_dir(m, c):
    path = m + "_manga"
    try: 
        os.mkdir(path)
    except:
        pass
    return path

def download_chapter(urls, path, manga, chapter):
    for i in urls:
        u = requests.get(i)
        with open(os.getcwd() + "/" + path + "/ " + manga + " " + chapter + " " + str(urls.index(i)) + ".jpg", "wb") as f:
            f.write(u.content)
            print(os.getcwd() + "/" + path + "/ " + manga + " " + chapter + " " + str(urls.index(i)) + ".jpg")
        print(u.url)

"""
chapters = get_manga("naruto")
print(chapters)
urls = get_chapter_url("naruto", "2")
print(urls)
download_chapter(urls, make_dir("naruto"), "naruto", "2")
"""

def download_chapter_menu(manga, chapter):
    path = make_dir(manga, chapter)
    urls = get_chapter_url(manga, chapter)[0]
    #download_chapter(urls, path, manga, chapter)
    for i in urls:
        u = requests.get(i)
        with open(os.getcwd() + "/" + path + "/ " + manga + " " + chapter + " " + str(urls.index(i)) + ".jpg", "wb") as f:
            f.write(u.content)
            print(os.getcwd() + "/" + path + "/ " + manga + " " + chapter + " " + str(urls.index(i)) + ".jpg")
        print(u.url)



def pick_chapter(manga):
    global l2
    global e2
    global b2
    global lb1
    l1.destroy()
    e1.destroy()
    b1.destroy()
    m = get_manga(manga)
    chapter = tk.IntVar()
    lb1 = tk.Listbox(screen)
    lb1.grid(row=0, column=0)
    for i in range(len(m)):
        lb1.insert(tk.END, m[i].replace("\n", ""))
    l2 = tk.Label(screen, text="choose chapter:")
    l2.grid(row=0, column=1)
    e2 = ttk.Entry(screen, textvariable=chapter)
    e2.grid(row=0, column=2)
    b2 = ttk.Button(screen, text="Submit", command=lambda: download_chapter_menu(manga, str(chapter.get())))
    b2.grid(row=1, column=1)


def main():
    global l1
    global e1
    global b1
    manga = tk.StringVar()
    l1 = tk.Label(screen, text="choose manga:")
    l1.grid(row=0, column=0)
    e1 = ttk.Entry(screen, textvariable=manga)
    e1.grid(row=0, column=1)
    b1 = ttk.Button(screen, text="Submit", command=lambda: pick_chapter(manga.get().replace(" ", "-")))
    b1.grid(row=1, column=0)

if __name__ == "__main__":
    main()

screen.mainloop()
