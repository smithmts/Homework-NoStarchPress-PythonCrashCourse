# Write a series of conditional tests.
# For each test, print your prediction.
# 5 (ended up with 6) Resulting in True, 5 Resulting in False.

# String Equal
casino = 'Luxor'
print("Is casino == 'Luxor'?  Predict True")
print(casino == 'Luxor')

# String Equal, Expect False
print("Is casino == 'Flamingo'?  Predict False")
print(casino == 'Flamingo')

# String Unequal
print("Is casino != 'Flamingo'? Predict True")
print(casino != 'Flamingo')

# String Unequal, Expect False
print("Is casino != 'Luxor'? Predict False")
print(casino != 'Luxor')

# Number Equal
winnings = 13
print("Are winnings == 13?  Predict True")
print(winnings == 13)

# Number Unequal
print("Are winnings != 1000000?  Predict True")
print(winnings != 1000000)

# Number Equal, Expect False
print("Are winnings == 1000000? Predict False")
print(winnings == 1000000)

# Number Unequal, Expect False
print("Are winnings != 13? Expect False")
print(winnings != 13)

# List Equal
casinos = ['Luxor','Flamingo']
print("Is 'Luxor' in casinos?  Predict True")
print('Luxor' in casinos)

# List Equal, Expect False
print("Is 'New York New York' in casinos? Predict False")
print('New York New York' in casinos)

# List Unequal
print("Is 'New York New York' in casinos?  Predict True")
print('New York New York' not in casinos)
