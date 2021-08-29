import json


colors = {"rainbow": ["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
          "CMYK": ["cyan", "magenta", "yellow", "key color"],
          "RBG": ["red", "blue", "green"]}

# write your code here
colors_json = json.dumps(colors)

with open("colors.json", "w", encoding="utf-8") as file:
    file.write(colors_json)