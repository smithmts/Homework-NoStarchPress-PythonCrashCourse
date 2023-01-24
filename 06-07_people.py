# Start with 06-01
# Make two new dictionaries for different people
# Store all three in a list named 'people'
# Loop through to print all known info about each.

person_01 = {
        'first_name': 'matthew',
        'last_name': 'smith',
        'age': 34,
        'city': 'imperial',
        }

person_02 = {
        'first_name': 'john',
        'last_name': 'doe',
        'age': 27,
        'city': 'el centro',
        }

person_03 = {
        'first_name': 'jane',
        'last_name': 'buck',
        'age': 42,
        'city': 'calexico',
        }

people = [person_01, person_02, person_03]

for person in people:
    full_name = f"{person.get('first_name')} {person.get('last_name')}"
    print(f"{full_name.title()}")
    print(f"\tAge: {person.get('age')}")
    print(f"\tCity: {person.get('city').title()}")


