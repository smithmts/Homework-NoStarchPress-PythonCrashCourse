# Chapter 8

# Functions with Return Values

def get_formatted_name(first_name, last_name):
    """Return a full naem, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# When using a return value, you need to provide a variable to which
# the result of the function is assigned.

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
