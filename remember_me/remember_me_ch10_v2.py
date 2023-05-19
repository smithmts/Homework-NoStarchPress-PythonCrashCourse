# Chapter 10

# Store and Retrieve User Generated Data in the Same Program

import json

# Load the username if stored previously.
# Prompt for the username and store it otherwise.
# Result is that it will ask for a username the first time, and then
# greet the user every time thereafter.

filename = 'username.json'

try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")
