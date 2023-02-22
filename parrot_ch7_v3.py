
# Chapter 7

# To not print anything for 'quit' input.
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Initalizes a blank message.
message = ""

while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
