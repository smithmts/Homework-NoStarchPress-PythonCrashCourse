# Chapter 7

# Make your prompts clear.
name = input("please enter your name: ")
print(f"\nHello, {name}!")

print("...")

# Assign the prompt to a variable, and build it over multiple lines.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")

print("...")

# Using input() to obtain a numerical value, it will be stored as
# a string.

age = input("How old are you? ")
print(age)

# You can print, but a numeric test will result in a TypeError
# age >= 18

# Converting using int() will avoid this.
age = int(age)
print(age >= 18)
