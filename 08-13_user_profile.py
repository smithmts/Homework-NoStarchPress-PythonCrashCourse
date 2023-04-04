# Start with a copy of user_profile.py
# Build a profile of your self by calling build_profile(), using first
# and last name and three other key-value pairs that describe you.

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('matthew', 'smith', location='imperial',
                            favorite_color = 'grey',
                            favorite_text_editor = 'neovim')

print(user_profile)

