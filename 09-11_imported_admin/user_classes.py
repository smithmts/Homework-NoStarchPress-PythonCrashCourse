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
