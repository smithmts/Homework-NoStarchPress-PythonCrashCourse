# Chapter 10

# Exceptions

# This would generage a tracebak error: `print(5/0)`

# Using `try-except` block:
try:
    print(5/0)
except ZeroDivisionError:  # Only runs if `try` block causes an error.
    print("You can't divide by zero!")
