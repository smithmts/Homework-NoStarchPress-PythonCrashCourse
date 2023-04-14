# Make a class called `Restaurant`.
# `__init__` method should `restaurant_name` and `cuisine_type`.
# Make a method called `describe_restaurant()` that prints these two
# pieces of information, and a method called `open_restaurant` that
# prints a message indicate that the restaurant is open.
# Make an instance called `restaurant` from your class.
# Print the two attributes individually, then call both methods.

class Restaurant:
    """Simple modeling of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print name and cuisine type attributes."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Simulate a restaurant opening."""
        print(f"{self.restaurant_name} is now open.")


restaurant_1 = Restaurant('El Zarape', 'Mexican')

print(restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
