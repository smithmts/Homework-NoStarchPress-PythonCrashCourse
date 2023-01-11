# Tests for equality and inequality with strings.
# testing using the lower() method.
# Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to.
# Use and keyword, or keyword.
# Item in a list, not in a list.

# String Equal Using lower()
casino = 'Luxor'
print("Is casino (case insensitive)=='Luxor'?  Predict True")
print(casino.lower() == 'luxor')

# Set Variables 
winnings = 13
played = 20

# Greater Than
print("Winnings Greater Than 10? Expect True")
print(winnings > 10)

# Less Than
print("Winnings Less Than A Million? Expect True")
print(winnings < 1000000)

# Less Than or Equal To
print("Played 100 or Less? Expect True")
print(played <= 100)

# Less Than, Greater Than, and keyword.
print("Winnings Greater Than 10 AND Less Than A Million? Expect True")
print(winnings > 10 and winnings < 1000000)

# Greater Than, Less Than or Equal To, or Keyword 
print("Winnings Greater Than 100 or Played At Least 20? Expect True") 
print(winnings > 100 or played >= 20)

# Item in a list. 
casinos = ['Luxor','Flamingo']
print("Flamingo in casinos? Expect True")
print('Flamingo' in casinos)

# Item not in a list.
print("Bellagio not in casinos? Expect True")
print('Bellagio' not in casinos)
