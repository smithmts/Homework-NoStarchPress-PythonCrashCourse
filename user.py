# Chapter 6 - Dictionaries

# Looping through a dictionary using for loop using items method.
user_0 = {
        'username': 'efermi',
        'first': 'enrico',
        'last': 'fermi',
        }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
# items returns a list of key value pairs.

# Can abbreviate.
for k, v in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
