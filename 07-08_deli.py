# Make a list called sandwitch_orders and fill it with the names of 
# various sandwitches.
# Loop through the list and print a message for each order.
# As each sandwich is mad, move to as list of finished sandwiches.
# After all sandwiches have been made, print a message listing each.

sandwitch_orders = ['turkey', 'pastrami', 'roast beef', 'cuban']
finished_sandwitches = []

while sandwitch_orders:
    current_sandwitch = sandwitch_orders.pop()
    print(f"Making your {current_sandwitch.title()} sandwitch.")
    finished_sandwitches.append(current_sandwitch)

print("\nThe following sandwitches are finished:")
for finished_sandwitch in finished_sandwitches:
    print(finished_sandwitch.title())
