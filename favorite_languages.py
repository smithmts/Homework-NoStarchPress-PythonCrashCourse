# Use a dictionary for several like items instead of differing ones.
# Also exmaple of multi-line formatting for dictionary.

favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }
# It's considered good practice to leave trailing comma for
# dictionaries so that you are ready to add the next pair.

print(favorite_languages)

# Use dictionary to look up value for particular person.

language = favorite_languages['sarah'].title()
print(f"Sara's favorite language is {language}.")


# for loop using items method
# instead of key, value or k, v, you can define your own variables.
# Makes most since if the same information type is stored in each key.

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# If only interested in the key, use keys method.
for name in favorite_languages.keys():
    print(name.title())

# ...or omit explicit keys method, since this is the default behavior.
for name in favorite_languages:
    print(name.title())

# Loop through keys and conditionally also return the value.
friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language.title()}!")

# Check to see if someone is in the dictionary.
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Starting with Python 3.7, dictionary items are returned in the order
# they were inserted.  Can sort as desired.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# Print just the values using the values method.
# Does not remove duplicates.
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("-----------")
# Wrap with set method to only show unite items.
for language in set(favorite_languages.values()):
    print(language.title())

# Sets are also defined by braces, but are not in key/value pairs.
languages = {'python','ruby','python','c'}
print("-----------")
print(languages)
