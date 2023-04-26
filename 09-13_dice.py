# Make a class `Die` with one attribute called `sides`, which has a
# default value of 6.
# Write a method called `roll_die()` that prints a random number
# between 1 and the number of sides the die has.
# Make a 6-sided die.
# Roll it 10 times.

from random import randint


class Die:
    """Simulate a roll-able die."""

    def __init__(self, sides=6):
        """Initialize sides attribute."""
        self.sides = sides

    def roll_die(self):
        """Simulate rolling a die."""
        print(randint(1, self.sides))


my_die = Die()

# Remebered to use `for` loop on a range from Chapter 4 :)
for value in range(0, 10):
    my_die.roll_die()
