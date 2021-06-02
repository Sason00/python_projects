import requests
from bs4 import BeautifulSoup
import os

manga = input("what manga do you want to download? ") # boruto-naruto-next-generations
url = requests.get("http://www.mangareader.net/" + manga)
soup = BeautifulSoup(url.text, "html.parser")

table = soup.find("table", {"class":"d48"})

cs = []
g = 0
for i in table.find_all("td"): 
    if g % 2 == 0:
        print(g // 2)
        print(i.text)
        cs.append(str(g//2))
    g += 1

g //= 2
print(g)

for chapter in cs:
	chapter = str(int(chapter) + 1)
	url = requests.get("http://www.mangareader.net/" + manga + "/" + chapter)
	soup = BeautifulSoup(url.text, "html.parser")

	pages = int(str(requests.get("http://www.mangareader.net/" + manga + "/" + chapter + "/99999999").url).split("/")[-1])
	urls = []

	for i in range(1, pages + 1):
		url = requests.get("http://www.mangareader.net/" + manga + "/" + chapter + "/" + str(i))
		soup = BeautifulSoup(url.text, "html.parser")
		src2 = soup.find("img")
		urls.append("https:" + str(src2["src"]))
		print("chapter: " + chapter, "page:", i, "https:" + str(src2["src"]))

	path = manga + "_manga"
	try: 
		os.mkdir(path)
	except:
		pass
	
	for i in urls:
		u = requests.get(i)
		with open(os.getcwd() + "/" + path + "/ " + manga + " " + chapter + " " + str(urls.index(i)) + ".jpg", "wb") as f:
			f.write(u.content)
			print("work", os.getcwd() + "/" + path + "/ " + manga + " " + chapter + " " + str(urls.index(i)) + ".jpg")

