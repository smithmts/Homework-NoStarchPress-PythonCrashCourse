# Chapter 6 - Dictionaries

alien_0 = {'color': 'green','points': 5}
print(alien_0['color'])
print(alien_0['points'])

# Example:  lookup how many points player earnes if shooting it down.
new_points = alien_0['points']
print(f"you just earned {new_points} points!")

# Add new key value pairs.
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Start with an empty dictionary and populate from there.
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5 
print(alien_0)

# Modify a dictionary value.
print(f"The color of the alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The color of the alien is {alien_0['color']}.")

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

# Change speed to fast.
alien_0['speed'] = 'fast'

# Delete a key-value pair.
print(alien_0)
del alien_0['points']
print(alien_0)
