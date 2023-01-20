# Chapter 6 - Dictionaries

alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Example:  lookup how many points player earnes if shooting it down.
new_points = alien_0['points']
print(f"you just earned {new_points} points!")

print("...") # My personal divider between activites in output.

# Add new key value pairs.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print("...")

# Start with an empty dictionary and populate from there.
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5 
print(alien_0)

print("...")

# Modify a dictionary value.
print(f"The color of the alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The color of the alien is {alien_0['color']}.")

print("...")

# Example:  tracking alien movement.
alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium','points': 5}
print(f"Original position: {alien_0['x_position']}")

# Determine how far to move the alien based on current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Speed must be fast.
    x_increment = 3

# New x_position is old position plus increment.
alien_0['x_position'] = alien_0['x_position'] = x_increment
print(f"New position: {alien_0['x_position']}")

print("...")

# Change speed to fast.
alien_0['speed'] = 'fast'

# Delete a key-value pair.
print(alien_0)
del alien_0['points']
print(alien_0)

print("...")

# Nesting - Establish 3 dictionaries and add to list.

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

print("...")

# More realistic example automatically populating dictionary.

# First make an empty list to store.
aliens = []

# Make 30 green aliens using range method.
for alien_number in range(30):
    new_alien = {'color': 'green','points': 5, 'speed': 'slow',} 
    aliens.append(new_alien)

# Print the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

print("...")

# Use a for loop to modify the first 3 aliens.
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Print the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...")

# Expand to turn green to yellow, and yellow to red.
# Since doing this after the for loop changing 3 to yellow, expecting
# to end up with 3 red and 2 green.

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Print the first 5 aliens.
for alien in aliens[:5]:
    print(alien)

print("...")
