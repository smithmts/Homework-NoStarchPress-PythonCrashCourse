# Use a dictionary to create a glossary of 5 terms learned about in
# previous chapters, with term as the key and definition as the value.
# Print each term and definition neatly, using new lines, etc.

glossary = {
        'variable': 'A named piece of information that is assigned a value',
        'list': 'A collection of items in a particular order',
        'index': 'A specific location within a variable',
        'if statement': 'A way to examine the current state and respond',
        'dictionary': 'A collection of related information in key/value pairs',
        }

# Again, I would really like to use a for loop or equilivalent here.
print(f"Variable:\n{glossary.get('variable')}\n")
print(f"List:\n{glossary.get('list')}\n")
print(f"Index:\n{glossary.get('index')}\n")
print(f"If Statement:\n{glossary.get('if statement')}\n")
print(f"Dictionary:\n{glossary.get('dictionary')}\n")
