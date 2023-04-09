# Chapter 8

# Modifying a list in a function.

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_modesl after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# Could have combined both steps into one function.
# However, each function should have one job for better extensibility.
# You can always use a function to call two other functions.


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
