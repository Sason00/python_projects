import requests
from bs4 import BeautifulSoup

# tw-interactive tw-link tw-link--hover-underline-none tw-link--inherit
# tw-interactive tw-link tw-link--hover-underline-none tw-link--inherit

input1 = input("what game do you want?")
url = requests.get("https://www.twitch.tv/directory/game/" + input1)
url_bs4 = BeautifulSoup(url.content, "html.parser")
online_stremers = url_bs4.find_all(
    "a")

print("hi")
for i in online_stremers:
    print(i)
    print("h")
h = url_bs4.find("a")
print(h.prettify())
