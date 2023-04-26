# Chapter 9

# Python Standard Library

from random import randint, choice
# These modules are part of the Python standard libary included with
# every Python installation.

# Generates a random number between 1 and 6.
print(randint(1, 6))

print("...")

# Take in a list/truple and return a randomly chosen element.
players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)
