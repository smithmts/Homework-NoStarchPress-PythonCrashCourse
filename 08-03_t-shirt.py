# Write a cunction called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt.
# The function should print a sentence smmarizing the size of the
# shirt and the message printed on it.
# Call the function once using positional arguments, and once using
# keyword aurguments.

def make_shirt(size, message):
    """Takes a size and message, and prints result."""
    print(f"\nYour size {size} shirt will have the following message:")
    print(message)

make_shirt('XL', 'Being devoured by Python is not so bad.')

make_shirt(message='Being devoured by Python is not so bad.', size='XL')
