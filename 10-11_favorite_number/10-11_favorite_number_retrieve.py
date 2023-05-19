import json

filename = 'favorite_number.json'

with open(filename) as f:
    fave_num = json.load(f)
    print(f"Your favorite number is {fave_num}.")
