# Use for loop to print all names in the list.
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

# for loop sets 'magician' as a variable, pulling items from
# 'magicians'. for loop is repeated for each item in the list.

# printing a message
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    # All lines in the indent are part of this for loop.
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone.  That was a great magic show!")
