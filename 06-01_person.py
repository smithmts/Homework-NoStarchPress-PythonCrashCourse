# Store information about a person you know.
# Store first name, last name, age, and city in which they live.
# Print each.

# Will go with line break format whenever likely to exceed 80 char.
person = {
        'first_name': 'matthew',
        'last_name': 'smith',
        'age': 34,
        'city': 'imperial',
        }

# Will always use get method for error protection.
# Practiced chaining 'dot' methods together.
print(person.get('first_name').title())
print(person.get('last_name').title())
print(person.get('age'))
print(person.get('city').title())
