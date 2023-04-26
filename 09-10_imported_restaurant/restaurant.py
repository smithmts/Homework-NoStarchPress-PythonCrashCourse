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
