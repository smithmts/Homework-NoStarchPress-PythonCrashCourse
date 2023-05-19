import json

fave_num = input("What is your favorite number? ")

filename = 'favorite_number.json'

with open(filename, 'w') as f:
    json.dump(fave_num, f)
    print(f"We'll remember that your favorite number is {fave_num}.")
