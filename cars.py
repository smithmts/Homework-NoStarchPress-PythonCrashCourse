# sort function permanently sorts the list.
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)

print("Here is the reverse list:")
print(cars)

# sorted is a temporary sort.

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the reverse list again")
print(cars)

# Length
print(len(cars))

# Chapter 5
# For loop with if statement.
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Single equal (=) is a statement.  Double equal (==) is a question.
# Check for equality regardless of case.
print(cars[3].lower() == 'audi')
