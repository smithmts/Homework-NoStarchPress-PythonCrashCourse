# Chapter 6
# Nesting a dictionary in a dictionary

users = {
        'aeinstein': {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princeton',
            },
        'mcurie': {
            'first': 'maire',
            'last': 'curie',
            'location': 'paris',
            },
    }

# Use for loop to setup variables, and then print

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

# This example was easier because we ensured that each dictionary had
# the same sub-dictionary
