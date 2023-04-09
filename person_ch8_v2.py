# Chapter 8

# Functions returning a more complex dictionary.

# Use `None` to indicate no specific value.
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {
            'first': first_name,
            'last': last_name,
            }
    # None equates to false.
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# Book gives example with age provided via keyword argument, but
# looked compatable with positional argument.  Tested/confirmed.
musician = build_person('jimi', 'hendrix', 27)
print(musician)
