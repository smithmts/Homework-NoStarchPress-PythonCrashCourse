# Make a list of >=5 usernames.
# Loop through the list and show greeting for each.
# For user 'admin' show a message that is special.

usernames = ['phineas','ferb','buford','admin','baljeet']

for username in usernames:
    if username == 'admin':
        print("Hello Admin. Would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")
