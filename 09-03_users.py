# Make a class called `User`.
# Make attributes `first_name` and `last_name` and several others that
# are typically stored in a user profile.
# Make a method called `describe_user()` that prints a summary of the
# users information.
# Make another method called `greet_user()` that prints a personalized
# greeting to the user.
# Create several instances and call both methods for each.

class User:
    """Model a user."""

    def __init__(self, first_name, last_name, username, email_address,
                 location):
        """Initialize user fields."""
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email_address = email_address
        self.location = location

    def describe_user(self):
        """Summarize user details."""
        print(f"User: {self.username}")
        print(f"\tFirst Name: {self.first_name}")
        print(f"\tLast Name: {self.last_name}")
        print(f"\tEmail:{self.email_address}")
        print(f"\tLocation: {self.location}")

    def greet_user(self):
        """Display a customized greeting to the user."""
        print(f"Hello {self.first_name}!")


user_1 = User('Phineas', 'Flynn', 'pflynn', 'pflynn@summer.bros', 'USA')
user_2 = User('Ferb', 'Fletcher', 'ffletcher', 'ffletcher@summer.bros', 'USA')
user_3 = User('Candace', 'Flynn', 'cflynn', 'cflynn@busted.look', 'USA')
user_4 = User('Perry', 'Platybus', 'agentp', 'p@owca.net', 'Tasmania')
user_5 = User('Heinz', 'Doofenshmirtz', 'hdoofenshmirtz', 'ruler@evilinc.com',
              'Drusselstein')
user_6 = User('Francis', 'Monogram', 'mmonogram', 'mm@owca.net', 'USA')

user_1.describe_user()
user_2.describe_user()
user_3.describe_user()
user_4.describe_user()
user_5.describe_user()
user_6.describe_user()

user_1.greet_user()
user_2.greet_user()
user_3.greet_user()
user_4.greet_user()
user_5.greet_user()
user_6.greet_user()
