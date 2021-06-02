import requests
from bs4 import BeautifulSoup
from bottle import run, route, get, post, request, template

def get_manga(manga):
    #manga = input("what manga do you want to download? ")
    url = requests.get("http://www.mangareader.net/" + manga)
    soup = BeautifulSoup(url.text, "html.parser")

    table = soup.find("table", {"id":"listing"})
    chapters = []
    g = 0
    for i in table.find_all("td"): 
        if g % 2 == 0:
            chapters.append(i.text)
        g += 1

    g //= 2
    return chapters

def get_chapter_url(manga, chapter):
    #chapter = input("what chapter do you wont to download(number)? ")
    url = requests.get("http://www.mangareader.net/" + manga + "/" + chapter)
    soup = BeautifulSoup(url.text, "html.parser")

    pages = int(soup.find("select", {"id":"pageMenu"}).find_all("option")[-1].text)
    urls = []

    for i in range(1, pages + 1):
        url = requests.get("http://www.mangareader.net/" + manga + "/" + chapter + "/" + str(i))
        soup = BeautifulSoup(url.text, "html.parser")
        urls.append(soup.find("img", {"id":"img"})["src"])
    return urls

@route("/")
def start():
    return template("/Users/rylwrn/Desktop/random_things/free_manga_downloader_template1.html")

@route("/watch")
def watch():
    global manga
    manga = request.query.manga
    return template("/Users/rylwrn/Desktop/random_things/free_manga_downloader_template2.html", chapters=get_manga(manga))

@route("/read")
def read():
    return template("/Users/rylwrn/Desktop/random_things/free_manga_downloader_template3.html", pages=get_chapter_url(manga, request.query.chapter))

run(host="localhost", port=8080)