# Chapter 8

# Mixing positional and arbitrary arguments.
# Python will match positional and keyword arguments first, then
# collect any remaining arguments in the final parameter.

# Arbitrary parameters must come after any positional ones.
def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a size {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")

make_pizza(16, 'pepperoni')
print("...")
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Book states you will often see the generic parameter name 8args,
# which collects arbitrary positional arugments.
