# Chapter 10

# Opening a file in append mode.

filename = 'programming.txt'

# 'a' opens the file in append mode.
# Any pre-existing data will remain.
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
