# Chapter 10

# Retrieve User-Generated Data

import json

filename = 'username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")
