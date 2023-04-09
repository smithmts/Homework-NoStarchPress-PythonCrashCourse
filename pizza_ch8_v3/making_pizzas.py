# Import the make_pizza() function from pizza.py

import pizza
# Code is copied into the file behind the secenes just before the
# program is run.
# This method inports the entire module and all functions therein.
# If pizza.py had multiple functions and we only wanted to import the
# one, this statement would do this:
# from pizza import make_pizza

# Now use the function contained in pizza
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# At least in my testing, specific function import requires omitting
# 'pizza.'
