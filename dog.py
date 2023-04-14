# Chapter 9

# Creating a Class

# Capitalized names used for Python classes.
class Dog:
    """A simple attempt to model a dog."""

    # Leading and trailing spaces prevent conflicts with Python's
    # method names (I don't fully understand that yet), and will
    # cause itto run automaticaly when the class is used (that I think
    # I understand.
    # `self` parameter needs to be first.
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
    # Prepending with `self` makes these available to every method
    # in the class.  These are called _attributes_.

    # `self` parameter is referenced throughout the class, and does
    # not need to be explicitly passed.
    # No additional information needs to be passed to `sit` and
    # `roll_over`
    def sit(self):
        """Simulate a dog sitting in respond to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a comand."""
        print(f"{self.name} rolled over!")


# This creates an instance of `Dog` as defined by the `__init__`
# method.  It is assigned to the variable `my_dog`.
my_dog = Dog('Willie', 6)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Dot notation can be used to call methods against a class instance.
my_dog.sit()
my_dog.roll_over()

print("...")

# You can create multiple instances.
your_dog = Dog('Lucy', 3)

print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
