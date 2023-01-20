# Make a dictionary with three major rivers and the country each 
# runs through.  Key is river, Value is country.
# Use a loop to print a sentance about each river including key and 
# value.
# Use a loop to print each river and one to print each country.

rivers = {
        'xingu': 'brazil',
        'ob': 'russia',
        'st lawrence': 'canada and united states',
        }

for river, country in rivers.items():
    print(f"The {river.title()} River is in {country.title()}.")

print("-------")

for river in rivers.keys():
    print(river.title())

print("-------")

for country in rivers.values():
    print(country.title())
