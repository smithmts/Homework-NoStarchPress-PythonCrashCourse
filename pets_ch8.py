# Chapter 8

# Function using positional arguments.

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
# `animal_type` and 'pet_name' arguments need to be provided in that
# order.

# Function can be called multiple times.
describe_pet('dog', 'willie')

# Mix up the arguments, get mixed up results.
describe_pet('harry', 'hamster')


# Keyword arguments allow you to specify argument-parameter
# relationship and provide in any order.
describe_pet(pet_name='harry', animal_type='hamster')
