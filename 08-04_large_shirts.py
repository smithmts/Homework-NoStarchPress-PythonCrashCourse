# Modify the make_shirt() function so that shirts are large by default
# with a message that reads I love Python.  Make a large shirt and a
# medium shirt with the default message, and a shirt of any size with
# a different message.

def make_shirt(size='L', message='I Love Python'):
    """Takes a size and message, and prints result."""
    print(f"\nYour size {size} shirt will have the following message:")
    print(message)


make_shirt()

make_shirt(size='M')

make_shirt(message='Being devoured by Python is not so bad.')
