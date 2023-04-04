# Write a function that accepts a list of items a person wants on a 
# sandwich.
# One parameter should collect as many items as the function call
# provides, and print a summary of the sandwitch that's being ordered.
# Call the function three times with a different list of arguments.

def make_sandwitch(*ingredients):
    """Make a sandwitch from provided ingredients."""
    print("\nYour sandwitch will be prepared with the following ingredients:")
    for ingredient in ingredients:
        print(f"-{ingredient.title()}")

make_sandwitch('pastrami','swiss cheese')
print('...')
make_sandwitch('roast beef','cheddar cheese', 'thousand island dressing')
print('...')
make_sandwitch('turkey','provologne', 'mustard', 'avocado')
