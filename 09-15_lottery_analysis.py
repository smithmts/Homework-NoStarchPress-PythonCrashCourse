# Make a list/tuple called `my_ticket`.
# Wtite a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give
# you a winning ticket.
# I'm not sure if the intent is for the winning ticket to change very
# time or be the same.  Latter is both more difficult to model and more
# like the real world, so let me try to do that.

from random import choice


# Aha!  Big brain over here using a function to for the random ticket
# assignments.
def four_random_chars():
    return f"{choice(list)}{choice(list)}{choice(list)}{choice(list)}"


# Assign the list of possible numbers/letters.
list = [2, 3, 5, 6, 12, 23, 35, 66, 72, 85, 'M', 'A', 'T', 'H', 'W']

# Initialize the variables.
entries = 0
my_ticket = four_random_chars()
winning_ticket = four_random_chars()


while my_ticket != winning_ticket:
    entries += 1
    my_ticket = four_random_chars()
    winning_ticket = four_random_chars()

print(f"{my_ticket} was a winner after {entries} entries.")
