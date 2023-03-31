# Writer a function called city_country() that takes the name of a 
# city and country.
# Return a string such as "Santiago, Chile"
# Call function 3 times

def city_country(city, country):
    """Return the name of a city and it's country"""
    print(f"{city.title()}, {country.title()}")

city_country('san diego', 'united states of america')

city_country('seattle', 'united states of america')

city_country('banff', 'canada')
