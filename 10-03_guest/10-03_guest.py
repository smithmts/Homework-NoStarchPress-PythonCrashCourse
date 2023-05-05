# Write a program that prompts the user for their name.
# Wrote their name to a file called guest.txt

filename = 'guest.txt'

username = input("Please enter your name: ")

with open(filename, 'w') as file_object:
    file_object.write(username)
