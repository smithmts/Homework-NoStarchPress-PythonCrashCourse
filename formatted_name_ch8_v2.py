# Chapter 8

# Functions with optional parameters.

# Can accomplish by adding blank default value, and address with 
# `if` statement.
# Don't forget to put defaulted parameter after any non-defaulted ones.
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full naem, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Don't forget to give argument for defaulted parameter last.
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
