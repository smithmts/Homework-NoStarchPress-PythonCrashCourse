
# Chapter 7

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
