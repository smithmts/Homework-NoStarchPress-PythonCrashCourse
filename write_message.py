# Chapter 10

# Writing to a file.

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
