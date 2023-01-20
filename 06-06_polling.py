# Use the code found in favorite_languages.py
# Make a list of people who should take the favorite languages pole.
# Include some names already in the dictionary and some that are not.
# Loop through the list of pople who should take the pole.  Print a
# message either thanking them for responding or inviting them to take
# the poll.


favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
        }

friends = [
        'jen',
        'sarah',
        'edward',
        'phil',
        'erin',
        'margaret',
        'robert',
        'isabella'
        ]

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"Thank you, {friend.title()}, for taking the poll!")
    else:
        print(f"{friend.title()}, would you mind taking the poll?")
