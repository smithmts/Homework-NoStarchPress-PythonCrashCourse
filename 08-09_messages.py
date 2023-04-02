# Make a list containing a series of short text messages.
# Pass the list to a function called show_messages(), which prints
# each message.

messages = [
        'Arguments can be passed posiitionally or using keywords.',
        'Defaulted parameters should be listed after any non-defaulted ones.',
        'Each function should have only one job.',
        'Pass a copy of a list to a function to prevent modification.'
        ]

def show_messages(messages):
    """Print all messages in a list"""
    for message in messages:
        print(message)

show_messages(messages)
