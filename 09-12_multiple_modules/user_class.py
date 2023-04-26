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
