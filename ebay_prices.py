import eel
import requests
from bs4 import BeautifulSoup
import time

eel.init("file:///Users/rylwrn/Desktop/python_projects/eel/ebay_prices_template.html")

# s-item__link


@eel.expose
def return_prices(product):
    ebay_url_string = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={}&_sacat=0".format(
        product)
    prices = []
    links = []
    ebay_url = requests.get(
        ebay_url_string)
    ebay_soup = BeautifulSoup(
        ebay_url.text, "html.parser")
    for i in ebay_soup.find_all(class_="s-item__price"):
        prices.append(str(i))
        print(i.text)
    for i in ebay_soup.find_all(class_="s-item__link", href=True):
        links.append(str(i["href"]))
        print(i["href"])
    time.sleep(1)
    for i in range(0, len(prices) - 1):
        eel.write_prices(prices[i], links[i])()
    print("finished")


eel.start("\\ebay_prices_template.html", size=(550, 612))
