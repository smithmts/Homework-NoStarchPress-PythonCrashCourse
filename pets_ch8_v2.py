# Chapter 8

# Function with defaulted argument.

def describe_pet(pet_name, animal_type='dog'):
# Defaulted parameters need to be after any non-defaulted ones for
# positional arguments to work correctly.
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

# Non-defaulted parameters are treated as positional.
describe_pet('willie')

# Can explicitly provide an argument other than the default.
describe_pet(pet_name='harry', animal_type='hamster')
