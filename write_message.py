# Chapter 10

# Writing to a file.

filename = 'programming.txt'

# 'w' opens the file in write mode.
# If the file does not exist, it will create it.
# If the file does exist, it will be erased--CAUTION!
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    # Only strings can be written to a test file.  Numerical data needs
    # to be converted to string format before writing.
