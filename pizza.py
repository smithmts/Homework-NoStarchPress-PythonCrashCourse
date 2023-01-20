# Chapter 6 - Dictionaries
# Nesting List inside Dictionary

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms','extra cheese'],
    }

# Summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza with the following toppngs:")

for topping in pizza['toppings']:
    print(f"\t{topping}")
