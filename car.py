# Chapter 9


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        # To always default an attribute, specify with assigned value
        # and do not include as a parameter.
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    # Create a method to modify an attribute's value.
    # Can also include protections against things like rolling back.
    def update_odometer(self, mileage):
        """
        Set the odometer reading to a given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    # Create method to incrementally update an attribute's value.
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        # Could add protections to prevent negative increments.


my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.read_odometer()

# Directly modify an attribute's value.
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Use a method to modify an attribute's value.
my_new_car.update_odometer(23_500)  # 23,500
my_new_car.read_odometer()

# Test attempt to provide value which is rejected by the method.
my_new_car.update_odometer(10)

# Use method to incrementally update an attribute's value.
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
