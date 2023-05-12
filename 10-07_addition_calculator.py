# Wrap activity 10-06 in a `while` loop so the user can continue
# entering numbers even if they make a mistake and enter text instead
# of a number

print("Enter numbers, and this program will add them for you.")
print("(Enter 'q' at any time to quit.)")

active = True
total = 0

while active:
    add_value = input("Enter a number: ")
    if add_value == 'q':
        print(f"Final total: {total}")
        active = False
    else:
        try:
            total += int(add_value)
        except ValueError:
            print("You can't add letters!")
        else:
            print(f"Current total: {total}")
