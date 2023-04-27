# Chapter 10

# Read a file line-by-line

# Can assign filename (or filepath) as a variable ahead of time instead
# of inside `open()`
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    # The file is closed once we exit this `with` block.  However,
    # we are reading it ito `lines` which we can continue working with.
    # `readlines()` stores each line of the file as an item in a list
    # with `\n` at the end.

for line in lines:
    print(line.rstrip())
    # `rstrip()` in this case prevents the output being essentially
    # double-spaced.
