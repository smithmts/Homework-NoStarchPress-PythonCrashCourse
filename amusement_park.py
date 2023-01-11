# Chapter 5

# if-elif-else chain.
age = 12
if age < 4:
    print("Your admission cost is $0")
elif age < 18:
    print("Your admission cost is $25")
else:
    print("Your admission cost is $40")

# More refined using variable.
age = 12
if age < 4:
    cost = 0
elif age < 18:
    cost = 25
else:
    cost = 40
print(f"Your admission cost is ${cost}")

# Add an additional elif block. 
age = 12
if age < 4:
    cost = 0
elif age < 18:
    cost = 25
else:
    cost = 40
print(f"Your admission cost is ${cost}")

# Add yet an additional elif block. 
age = 12
if age < 4:
    cost = 0
elif age < 18:
    cost = 25
elif age < 65:
    cost = 40
else:
    cost = 20 
print(f"Your admission cost is ${cost}")
