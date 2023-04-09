# Write a function that stores information about a car in a dictionary.
# The function should always receive a manufacturer and a model name.
# It should then accept an arbitrary of keyword arguments.
# Call the function with the required information and two other
# name-value pairs.
# Print the dictionary that returned to make sure all the information
# was stored correctly.

def make_car(manufacturer, model_name, **car_options):
    """Build a car as specified."""
    # The dictionary must be as defined in `def` line.
    car_options['manufacturer'] = manufacturer
    car_options['model_name'] = model_name
    return car_options


new_car = make_car('hyundai', 'tuscon', color='silver', drivetrain='hybrid')
print(new_car)
