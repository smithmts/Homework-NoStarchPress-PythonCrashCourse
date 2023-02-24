# Chapter 7

# `while` loops.

current_number = 1

# Starts with one, prints the number and adds one until it reaches 5.
while current_number <= 5:
    print(current_number)
    current_number += 1

print("...")

# Using a `continue` break

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

# `continue` starts loop over at the beginning, skipping the rest.
# current_number is still incremented because it preceeds the break,
# but the print operation is skipped.

# Always scrutanize `while` loops to make sure they are not infinate.
