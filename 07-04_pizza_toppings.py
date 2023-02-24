# Write a loop that prompts the user to enter a series of toppings
# until they enter a 'quit' value.
# As they enter each topping, print a message saying you'll add that
# topping to the pizza.

prompt = "\nEnter a topping, and I will add it to your pizza."
prompt += "\nEnter 'quit' to finish your pizza."
prompt += "\nEnter topping: "


# Wanna get fancy with it and print a list of toppings at the end.
toppings = []

active = True

while active == True:
    topping_entry = input(prompt)
    if topping_entry == 'quit':
        active = False
        print("\nYour pizza with the following toppings is being prepared:")
        for topping in toppings:
            print(f"\t{topping.title()}")
    else:
        toppings.append(topping_entry)
