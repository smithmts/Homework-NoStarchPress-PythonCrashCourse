# Start with Activity 09-01
# Create three instances.
# Call `describe_restaurant() for each instance.

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
restaurant_2 = Restaurant('Marechiaro\'s', 'Italian')
restaurant_3 = Restaurant('Panda Machi', 'Sushi')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
