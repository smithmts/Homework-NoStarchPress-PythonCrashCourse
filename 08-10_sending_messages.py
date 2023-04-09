# Start with a 08-09.
# Write a function called send_messages() that prints each text
# message and moves each message to a new list called sent_messages
# as it's printed.
# Print both of your lists to make sure they were moved correctly.


def show_messages(messages):
    """Print all messages in a list"""
    while messages:
        current_message = messages.pop()
        print(f"Sending Message: {current_message}")
        sent_messages.append(current_message)


messages = [
        'Arguments can be passed posiitionally or using keywords.',
        'Defaulted parameters should be listed after any non-defaulted ones.',
        'Each function should have only one job.',
        'Pass a copy of a list to a function to prevent modification.'
        ]

sent_messages = []

show_messages(messages)

print(messages)
print(sent_messages)
