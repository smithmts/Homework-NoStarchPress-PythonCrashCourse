# Start with Activity 09-01.
# Add an attribute called `number_served` with a default value of 0.
# Create an instance called restaurant.
# Print the number of customers the restaurant has served.
# Change the value and print it again.
# Add a method called `set_number_served() to set the number of of
# customers a restaurant has served, use it, and print the new value.
# Add a method called `increment_number_served()` that increments
# the number of customers served. Use the method and print new value.

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


restaurant = Restaurant('El Zarape', 'Mexican')

print(restaurant.number_served)

restaurant.number_served = 18
print(restaurant.number_served)

restaurant.set_number_served(28)
print(restaurant.number_served)

restaurant.increment_number_served(80)
print(restaurant.number_served)
