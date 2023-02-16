# Make a dictionary called cities.
# Name of the city is the key in that dictionary.
# Create a dictoinary of information about each city.
# Suggestion: population, county, fact.

cities = {
        'las vegas': {
            'state': 'nevada',
            'population': 641903,
            'fact': "One of the city's earliest attractions was divorce",
            },
        'san diego': {
            'state': 'california',
            'population': 1386932,
            'fact': "It is the first California location settled by europeans",
            },
        'seattle': {
            'state': 'washington',
            'population': 737015,
            'fact': "The city is named after Chief Si'hal",
            },
    }

# From "Many Cities Example"
# Use for loop to setup variables, and then print
for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tState: {city_info['state'].title()}")
    print(f"\tPopulation: {city_info['population']}")
    print(f"\tFact: {city_info['fact']}.")
