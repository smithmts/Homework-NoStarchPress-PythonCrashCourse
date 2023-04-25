# Write a class called `Admin` that inherits from the `User` class
# from Excersize 09-03 or 09-05
# Add a `privileges` attribute storing a list of strings like
# 'can add post', 'can delete post', 'can ban user' and so on.
# Write a method called `show_privileges()` that lists the administrator's
# set of privileges.
# Create an instance of `Admin` and call the method.

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


class Admin(User):
    """Represent aspects of a user specific to an administrator."""

    def __init__(self, first_name, last_name, username, email_address,
                 location):
        """Initialize user and administrator attributes."""
        super().__init__(first_name, last_name, username, email_address,
                         location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show user privileges."""
        print(f"Privileges for user {self.username} are as follows:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")


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

# Create our admin user.
user_7 = Admin('Alfred', 'Acronym', 'aacronym', 'aa@owca.net', 'USA')
user_7.describe_user()
user_7.show_privileges()
