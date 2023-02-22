# As the user how many people are in their dinner group.
# If the answer is more than eight, print a message that they will have
# to wait for a table.  Otherwise, print a message that their table is
# ready.

people_count = input("Please enter the number of people in your group: ")
people_count = int(people_count)

if people_count >= 8:
    print("There will be a 20 minute wait.")
else:
    print("We have a table ready for you.")
