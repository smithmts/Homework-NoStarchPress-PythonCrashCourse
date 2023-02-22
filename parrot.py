# Chapter 7

# Ask for input, then display back to the user.
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
# Text editors (including neovim in this case) generally cannot run
# this code.  It must be run directly in the terminal.

print("...")
# Let the user decide when to quit

# Sets a prompt in two steps.
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Initalizes a blank message.
message = ""

while message != 'quit':
    message = input(prompt)
    print(message)
# Will request input first time based on blank variable.
# For each input other than 'quit' will set message to the input and
# then print that message.
# Input of 'quit' will trigger end of the while loop.
# This version will print 'quit' the last time becasue that is the input
print("...")

# To not print anything for 'quit' input.
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Initalizes a blank message.
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
