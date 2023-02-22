# Chapter 7

prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# A flag is a variable that accounts for multiple conditions and
# determines if program should remain active.

# Create flag
active = True
# message variable no longer needs to be initialized since active
# sets initial condition for while loop to begin.

while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)
