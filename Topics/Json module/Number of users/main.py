# write your code here
import json

users_json = ""
with open("users.json", "r", encoding="utf-8") as file:
    users_json = json.load(file)

print(len(users_json['users']))