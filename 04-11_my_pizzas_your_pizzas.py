# Start with program from Excersize 4-1
#######################################################################
# Think of at least three kinds of pizza.
pizzas = ['pepperoni', 'sausage', 'pesto']

# Use for loop to print the name of each pizza.
for pizza in pizzas:
    print(pizza)

# Modify for loop to print a sentance.
for pizza in pizzas:
    print(f"Holy mother of god, I friggin love {pizza} pizza!")

# Add a line at the end of the program, outside the for loop.
for pizza in pizzas:
    print(f"Holy mother of god, I friggin love {pizza} pizza!")
print("I cannot overstate how much I love pizza.")
#######################################################################

# Make a copy of the list.
friend_pizzas = pizzas[:]
# Add something different to each list.
pizzas.append('whitestone')
friend_pizzas.append('mushroom')

# Print both lists using message and for loops.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)
