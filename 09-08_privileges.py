# Start from 09-07.
# Write a separate `Privileges` class.
# Class has single attribute, `privileges', which is the same as in
# 09-07.
# Move `show_privileges()` method to this class.
# make `Privileges' instance as attribute of `Admin` class.

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


class Privileges:
    """Model Privileges for a user."""

    def __init__(self, privileges=['can add post', 'can delete post',
                                   'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        """Show user privileges."""
        # print(f"Privileges for user {self.username} are as follows:")
        # Don't yet know how to reference attribute of class for which
        # an instance of this class is an attribute.
        print("Privileges for this user are as follows:")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")


class Admin(User):
    """Represent aspects of a user specific to an administrator."""

    def __init__(self, first_name, last_name, username, email_address,
                 location):
        """Initialize user and administrator attributes."""
        super().__init__(first_name, last_name, username, email_address,
                         location)
        self.privileges = Privileges()


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

user_7 = Admin('Alfred', 'Acronym', 'aacronym', 'aa@owca.net', 'USA')
user_7.describe_user()

# Call method updated find method in `Privileges` class.
user_7.privileges.show_privileges()
