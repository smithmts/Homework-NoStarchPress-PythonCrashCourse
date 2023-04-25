# Start with Activity 09-01 or 09-04 (Choosing 09-04)
# Write a class called `IceCreamStand` that inherits from the
# `Restaurant` class.
# Add an attribute called `flavors` that stores a list of ice cream
# flavors.
# Create an instance of `IceCreamStand` and call the method.

class Restaurant:
    """Simple modeling of a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Print name and cuisine type attributes."""
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Simulate a restaurant opening."""
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, served):
        """Set the number of customers a restaurant has served."""
        self.number_served = served

    def increment_number_served(self, served):
        """Increment the number of customers a restaurant has served."""
        self.number_served += served


class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant specific to Ice Cream Stands"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize Restaurant and Ice Cream Stand attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Berry Farcia', 'Phish Cticks', 'Vanilla']
        # I apparently don't know yet how to pass an additional init
        # parameter to the one in the parent class.  Not smart enough
        # to figure it out on my own at the moment.  Will have to
        # manually define like the electric car battery example.

    def list_flavors(self):
        """Print a list of flavors."""
        print(f"{self.restaurant_name} serves the following flavors.")
        for flavor in self.flavors:
            print(f"\t{flavor}")


restaurant = Restaurant('El Zarape', 'Mexican')
restaurant.describe_restaurant()

bob_and_jimmys = IceCreamStand('Bob & Jimmy\'s', 'Ice Cream Stand')
bob_and_jimmys.list_flavors()
