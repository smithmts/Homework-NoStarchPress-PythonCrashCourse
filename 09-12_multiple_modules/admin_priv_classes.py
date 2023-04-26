from user_class import User


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
