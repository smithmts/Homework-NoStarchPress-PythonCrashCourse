# Clean up the code from excersize 6-3 to use a loop.
# Add 5 more terms to the glossary.

glossary = {
        'variable': 'A named piece of information that is assigned a value',
        'list': 'A collection of items in a particular order',
        'index': 'A specific location within a variable',
        'if statement': 'A way to examine the current state and respond',
        'dictionary': 'A collection of related information in key/value pairs',
        'keys method': 'Used to loop through keys without values',
        'values method': 'Used to loop through values without keys',
        'set method': 'Used to loop through unique values in a dictionary',
        'sets': 'A group of unique items not in pairs, also wrapped in braces', 
        'default': 'The behavior of a program without alternative instructions',
        }

for term, definition in glossary.items():
    print(f"{term.title()}:\n{definition}.\n")
