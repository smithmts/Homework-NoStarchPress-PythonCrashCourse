# Write a function called describe_city() that accepts the name of a
# city and it's country.
# Give the parameter for the country a default value.
# Call the function for 3 different cities, at least oneof which is not
# in the default country.

def describe_city(city, country='the united states of america'):
    """Prints a city and the country it is in."""
    print(f"{city.title()} is in {country.title()}.")

describe_city('san diego')

describe_city('banff', 'canada')

describe_city('port angeles')
