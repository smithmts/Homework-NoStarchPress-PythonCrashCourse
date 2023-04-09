# Chapter 8

# Simple greeting function.

def greet_user():
    """Display a simple greeting."""
    # Functions are documented with a docstring.
    print("Hello!")


greet_user()

print("...")

# Function with single input.


def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")


greet_user('jesse')
# username in this example is a parameter.
# 'jesse' is the argument that was past to the function and assigned
# to the parameter.
