# From 5-8, add an if test to display special message if the list
# is empty.

usernames = []

if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello Admin. Would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")
