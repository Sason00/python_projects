import json

json_file = json.load(
    open("C:\\Users\\Ariel\\Desktop\\json files\\tutorial.json", "r"))
print(json_file)
json_file["num"] += 1
print(json_file)
