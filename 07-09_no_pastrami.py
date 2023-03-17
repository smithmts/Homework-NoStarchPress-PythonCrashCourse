# Using list from 07-08, make sure that 'pastrami' appears at least
# three times.
# Add code near the beginning of the program to print a message saying
# that the deli has run out of pastrami, and remove all occurances from
# the list using a while loop.
# No instances of 'pastrami' should appear in finished_sandwitches.

sandwitch_orders = ['turkey', 'pastrami', 'roast beef', 'pastrami', 'cuban', 'pastrami']
finished_sandwitches = []

print("Sorry, the deli is out of Pastrami.")
while 'pastrami' in sandwitch_orders:
    sandwitch_orders.remove('pastrami')

while sandwitch_orders:
    current_sandwitch = sandwitch_orders.pop()
    print(f"Making your {current_sandwitch.title()} sandwitch.")
    finished_sandwitches.append(current_sandwitch)

print("\nThe following sandwitches are finished:")
for finished_sandwitch in finished_sandwitches:
    print(finished_sandwitch.title())
