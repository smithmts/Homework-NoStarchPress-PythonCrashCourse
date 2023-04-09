# Start with a 08-10.
# Use a copy of messages to retain the original list.
# Print both lists to show that the original list remains unchanged.


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


show_messages(messages[:])

print(messages)
print(sent_messages)
