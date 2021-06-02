import requests
from bs4 import BeautifulSoup

input1 = input("enter here the episode url: ")
url1 = requests.get(input1)

print(url1)
"""
params = {
        "Host": "www.sdarot.work",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Content-Length": "35",
        "Origin": "https://www.sdarot.work",
        "Connection": "keep-alive",
        "Referer": input1,
        "Cookie": "_ga=GA1.2.751971807.1589816775; _gid=GA1.2.229234869.1594654215; warn_611=true; Sdarot=gp%2C7CiqFjNBVUaBSgIjQG2wFlVk2ntrsAciDohfY7xNhP1iydivdU6bXrZCxkSwSG3BLyz7Jb3Y3toqZgDl9s%2CmVnQO7fAjBx58jCT5NO8Zaduo%2C9CKPzX1yNuGoqu75",
        "TE": "Trailers"
    }
"""

params = {
        "Host": "minerva.sdarot.work",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:78.0) Gecko/20100101 Firefox/78.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Origin": "https://www.sdarot.work",
        "Connection": "keep-alive",
        "Referer": input1,
        "Cookie": "_ga=GA1.2.751971807.1589816775; _gid=GA1.2.229234869.1594654215; Sdarot=gp%2C7CiqFjNBVUaBSgIjQG2wFlVk2ntrsAciDohfY7xNhP1iydivdU6bXrZCxkSwSG3BLyz7Jb3Y3toqZgDl9s%2CmVnQO7fAjBx58jCT5NO8Zaduo%2C9CKPzX1yNuGoqu75"
}
url2 = requests.post(input1, data=params)
print(url2.headers)

