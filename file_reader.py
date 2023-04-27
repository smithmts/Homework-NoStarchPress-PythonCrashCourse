# Chapter 10

# Reading from a text file.

with open('pi_digits.txt') as file_object:
    # `open()` looks for the file in the same directory this program is
    # running.
    # `file_object` is the object we are assiginging to represent the
    # file.
    # Can manually use `close()` method, but this has to be done
    # Carefully.  `with` keyword allows Python to close the file when
    # no longer needed without you having to figure that out.
    contents = file_object.read()
    # `read()` takes the entire contents of the file and turns it into
    # a string, which we are assigning to the contents variable.
print(contents)
print("...")

# `read()` returns an exmpty string when it reaches the end of a file,
# which appears as a blank line.
# Can use `rstrip()` to remove it. You remember `rstrip()` removes
# whitespace charactrers from the right side of a string, right?
print(contents.rstrip())
print("...")
