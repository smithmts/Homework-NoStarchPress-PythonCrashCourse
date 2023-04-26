# Make a list/tuple containing series of 10 numbers and 5 letters.
# Randomly select 4 numbers/letters from the list and print a message
# saying that any ticket matching these for numebrs or letters wins
# a prize.

from random import choice

list = [2, 3, 5, 6, 12, 23, 35, 66, 72, 85, 'M', 'A', 'T', 'H', 'W']

# Not sure if there is a way to force unique selections when using the 
# `choice` method.  Possible duplicates will be a limitation for now.
winning_char_1 = choice(list)
winning_char_2 = choice(list)
winning_char_3 = choice(list)
winning_char_4 = choice(list)

print("Congratulations to the person with ticket:")
print(f"{winning_char_1} {winning_char_2} {winning_char_3} {winning_char_4}")
print("You win a prize!")
