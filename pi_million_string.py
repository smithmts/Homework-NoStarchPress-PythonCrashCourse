# Chapter 10

# Demostration that program works with (much) larger files.

filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()
    # Downloaded file from resources this time.

print(f"{pi_string[:52]}...")  # Print only the first 50, shall we?
print(len(pi_string))
