import json
import os

os.chdir("C:\\Users\Ariel\Desktop")
print(os.getcwd())
os.chdir("json files")
print(os.getcwd())

json_file = json.load(open("tutorial.json"))
#ch_json = open("tutorial.json", "w+")
#ch_json.write(json_file + """
#    "gg":"gg"
#                """)
#ch_json.close()
print(json_file)
