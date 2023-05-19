import json


def get_favorite_number():
    """Get stored favorite number if available."""
    filename = 'favorite_number.json'
    try:
        with open(filename) as f:
            fave_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fave_number


def get_new_favorite_number():
    """Prompt for a new favorite number."""
    fave_number = input("What is your favorite number? ")
    filename = 'favorite_number.json'
    with open(filename, 'w') as f:
        json.dump(fave_number, f)
    return fave_number


def display_favorite_number():
    """Display the user's favorite number."""
    fave_number = get_favorite_number()
    if fave_number:
        print(f"Your favorite number is {fave_number}.")
    else:
        fave_number = get_new_favorite_number()
        print(f"We'll remember that your favorite number is {fave_number}.")


display_favorite_number()
