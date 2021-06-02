from bs4 import BeautifulSoup
import requests
url = requests.get('https://he.wikipedia.org/wiki/מיינקראפט')
soup = BeautifulSoup(url.content)
print(soup.findAll("a"))
