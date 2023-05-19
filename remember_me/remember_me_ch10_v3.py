# Chapter 10

# Store and Retrieve User Generated Data in the Same Program
# ...Refactored

import json


def greet_user():
    """Greet the user by name."""
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


greet_user()

# I feel like the contents of `greet_user()` should be split into at
# least two separate functions.  Reading ahead, I appear to be right.
