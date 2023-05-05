# Chapter 10

# Writing multiple lines to a file.

filename = 'programming.txt'
# Original file will be erased and re-written since it exists and we
# are using write mode.

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")
    # Need to include newline character, or each added string will be
    # on the same line.
