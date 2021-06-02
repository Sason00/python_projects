import os
import requests
import time
from bs4 import BeautifulSoup as bs

print(time.localtime().tm_hour, ":",
      time.localtime().tm_min, ".", time.localtime().tm_sec)
# "path\to\chrome\chrome.exe" --app=http://facebook.com

input1 = input("path: ")
functions = ["alertime"]


def init(path):
    os.system("start chrome.exe" + " " + "--app=" + path)


def alertime():
    pass


def expose(name_or_function=None):
    # Deal with '@eel.expose()' - treat as '@eel.expose'
    if name_or_function is None:
        return expose

    if type(name_or_function) == str:   # Called as '@eel.expose("my_name")'
        name = name_or_function

        def decorator(function):
            _expose(name, function)
            return function
        return decorator
    else:
        function = name_or_function
        #_expose(function.__name__, function)
        return function


path = bs(open(input1, "r"), "html.parser").prettify()
init(input1)
print(path)
