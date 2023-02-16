# Create dictionary named favorite_places
# One name with 1-3 places for each person
# Loop through and print all info

favorite_places = {
        'matthew': ['forks','las vegas'],
        'kristen': ['san diego','las vegas','paso robles'],
        'katie': ['imperial','holtville'],
        }

for people, places in favorite_places.items():
    print(f"\n{people.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
