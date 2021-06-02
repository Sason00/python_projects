import requests

input1 = input("what to search?")
url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw="+ input1+"&_sacat=0"
web1 = requests.get(url)
print(web1.headers["s-item__price"])
