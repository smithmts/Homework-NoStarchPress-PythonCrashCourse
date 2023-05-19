# Chapter 10

# Storing Data using JSON

import json

numbers = [2, 3, 5, 7, 11, 13]

# it is customary to include the `.json` file extension.
filename = 'numbers.json'

# Don't forget to open file in write mode.
with open(filename, 'w') as f:
    json.dump(numbers, f)
    # Arguments for `json.dump() include what you want to store, and
    # what object you want to store it in.
