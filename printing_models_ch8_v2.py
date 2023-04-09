# Chapter 8

# Function working with a list with modificaitons prevented.

# Functions can remain unchanged.
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


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# If you want to use the function while keeping the unprinted_designs
# list unchanged, just pass a copy
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

# Only pass a copy when you have a reason, because this requires
# extra processing.

# Show that completed_models list has been populated, and that
# unprinted_designs remains unchainged.
print(unprinted_designs)
print(completed_models)
