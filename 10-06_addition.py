# Write a program that prompts the user for two numbers and adds them
# together
# Implement a ValueError exception that notifies the user when they
# enter a letter.

print("Enter two numbers, and this program will add them for you.")

try:
    first_number = int(input("First Number: "))
    second_number = int(input("Second Number: "))
except ValueError:
    print("You can't add letters!")
else:
    print(first_number + second_number)
