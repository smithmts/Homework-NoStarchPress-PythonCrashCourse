# Make dictionaries for several pets.
# Each could include the species and the owner.
# Put into a list named pets, and loop through to print all info.

pet_1 = {
        'name': 'ronny',
        'species': 'dog',
        'owner': 'michael',
        }
pet_2 = {
        'name': 'jill',
        'species': 'goldfish',
        'owner': 'karen',
        }
pet_3 = {
        'name': 'olly',
        'species': 'rabbit',
        'owner': 'raylee',
        }
pet_4 = {
        'name': 'bubble gum',
        'species': 'guinea pig',
        'owner': 'katie',
        }
pet_5 = {
        'name': 'stripes',
        'species': 'cat',
        'owner': 'doris',
        }
pet_6 = {
        'name': 'butch',
        'species': 'lizard',
        'owner': 'jessie',
        }

pets = [pet_1,pet_2,pet_3,pet_4,pet_5,pet_6]

for pet in pets:
    print(pet['name'].title())
    print(f"\tSpecies: {pet['species'].title()}")
    print(f"\tOwner: {pet['owner'].title()}")
