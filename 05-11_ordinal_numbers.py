# Store numbers 1-9 in a list.
# Use an if-elif-else chain to apply the proper ordinal ending for each
# number ('st','nd','rd','th').
# print each number on a new line.

ordinal_numbers = list(range(1,10))

for ordinal_number in ordinal_numbers:
    if ordinal_number < 2:
        print(f"{ordinal_number}st")
    elif ordinal_number < 3:
        print(f"{ordinal_number}nd")
    elif ordinal_number < 4:
        print(f"{ordinal_number}rd")
    else:
        print(f"{ordinal_number}th")
