# Modify 06-02 so that each person can have more than one number.
# Print each person's name along with their favorite numbers.

favorite_numbers = {
        'derek': [2,1311], # Want to swap out for a significant number.
        'lou': [4,1995],
        'joe': [5,1941],
        'mickey': [7,1509],
        'thurman': [15,701],
        }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")
