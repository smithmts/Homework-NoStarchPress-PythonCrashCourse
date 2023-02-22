# Chapter 7

# Modulo Operator
# Returns the remainder of a division operation.
# When number modulo 2 is equal to zero, the number is even.

number = input("Enter a numnber, and I'll tell you if it's even or odd ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe nunmber is even")
else:
    print(f"\nThe number is odd")
