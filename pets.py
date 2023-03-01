# Chapter 7

# Remove all instances of a specific value from list.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')  # Removes from beginning of list.

print(pets)
