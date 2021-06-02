from bs4 import BeautifulSoup
import requests

input1 = input("put here the youtuber you want to check ")
url = requests.get("https://www.youtube.com/results?search_query=" + input1)
source = BeautifulSoup(url.text, 'html.parser')

print(source)
