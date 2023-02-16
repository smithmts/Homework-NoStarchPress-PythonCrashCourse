# Use a dictionary to store 5 names as keys, and give each a favorite
# number.  Print each name and their number.

# Really want to use a for loop here, but it seems to use methods that
# haven't been covered yet.  Will move forward the less elegant way.

favorite_numbers = {
        'derek': 2,
        'lou': 4,
        'joe': 5,
        'mickey': 7,
        'thurman': 15,
        }

print(f"Derek's number is {favorite_numbers.get('derek')}") 
print(f"Lou's number is {favorite_numbers.get('lou')}") 
print(f"Joe's number is {favorite_numbers.get('joe')}") 
print(f"Mickey's number is {favorite_numbers.get('mickey')}") 
print(f"Thurman's number is {favorite_numbers.get('thurman')}") 
