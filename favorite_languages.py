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
