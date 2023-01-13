# Chapter 6 - Dictionaries

alien_0 = {'color': 'green','speed': 'slow'}

# Trying to ask for a key that does not exist results in a key error.
# print(alien_0['points'])

# Instead you can use the get method.  There is an optional argument to
# specify the returned value if the key doesn't exits. If you omit the
# second argument, it will default to "None."

point_value = alien_0.get('points','No point value assigned.')
print(point_value)
