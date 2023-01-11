# Make a list of >=5 usernames called current_users.
# Make another list of >=5 users called new users.  1-2 of the users 
# should be in both lists.
# Run a loop to present duplicates with a message indicating that they
# need to choose a new username.
# Ensure that test is case insensitive by creating a lowercase copy of
# the list.

current_users = ['phineas','Ferb','buford','Baljeet','isabella']

# Found through this excersize that you cannot user lower method on a
# list.  Solution that works with content covered in the book so far is
# to establish the blank second list, then use for loop with append and
# lower methods to populate the list form the first one.

current_users_lower = []
new_users = ['phineas','ferb','candace','lawrence','linda']

# for loop to establish current_users_lower
for current_user in current_users:
    current_users_lower.append(current_user.lower())

# Run the test.
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("You will need to enter a new username.")
    else:
        print(f"Username {new_user} has been created.")
