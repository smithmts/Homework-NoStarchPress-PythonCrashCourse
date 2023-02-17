# Use one of the example programs from this chapter, and extend it by adding
# keys and valuses, changing the context or improving the formatting
# of the output.

users = {
        'aeinstein': {
            'active' : 'no',
            'first': 'albert',
            'last': 'einstein',
            'roles': ['math','physics'],
            },
        'mcurie': {
            'active' : 'no',
            'first': 'maire',
            'last': 'curie',
            'roles': ['chemistry','physics'],
            },
        'msmith': {
            'active' : 'yes',
            'first': 'matthew',
            'last': 'smith',
            'roles': ['admin','history'],
            },
    }

# Use for loop to setup variables, and then print

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    roles = user_info['roles']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tActive: {user_info['active'].title()}")
    print(f"\tRoles:")
    for role in roles:
        print(f"\t\t{role}")
