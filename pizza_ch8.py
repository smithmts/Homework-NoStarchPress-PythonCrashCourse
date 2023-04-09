# Chapter 8

# Function with arbitrary number of arguments.

# parameter with `*` turns it into an empty tuple that is populated
# with whatever it receives as an argument.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"-{topping}")


make_pizza('pepperoni')
print("...")
make_pizza('mushrooms', 'green peppers', 'extra cheese')
