# Chapter 10

# Working wiht a file's contents.

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

# Create a variable to hold the single string.
pi_string = ''

# Add each line to `pi_string` without the whitespace.
for line in lines:
    pi_string += line.strip()
    # Author's file apparently had whitespce on the left that I did not
    # see/include.  `rstrip()` does the job for my file.

print(pi_string)
print(len(pi_string))
