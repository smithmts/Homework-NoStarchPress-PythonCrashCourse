# Start with Activity 09-03.
# Add and attribute called `login_attempts`
# Write a method called `increment_login_attempts()` that increments
# the number of attempts by 1.
# Write another method called `reset_login_attempts` that resets the
# value of `login_attempts` to 0.

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
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self.login_attempts += 1
        print(f"Incorrect password. Total Attempts: {self.login_attempts}.")

    def reset_login_attempts(self):
        """Reset the number of login attempts."""
        self.login_attempts = 0
        print(f"Login attempts reset to {self.login_attempts}")


user_1 = User('Phineas', 'Flynn', 'pflynn', 'pflynn@summer.bros', 'USA')
user_2 = User('Ferb', 'Fletcher', 'ffletcher', 'ffletcher@summer.bros', 'USA')
user_3 = User('Candace', 'Flynn', 'cflynn', 'cflynn@busted.look', 'USA')
user_4 = User('Perry', 'Platybus', 'agentp', 'p@owca.net', 'Tasmania')
user_5 = User('Heinz', 'Doofenshmirtz', 'hdoofenshmirtz', 'ruler@evilinc.com',
              'Drusselstein')
user_6 = User('Francis', 'Monogram', 'mmonogram', 'mm@owca.net', 'USA')

user_5.increment_login_attempts()
user_5.reset_login_attempts()
