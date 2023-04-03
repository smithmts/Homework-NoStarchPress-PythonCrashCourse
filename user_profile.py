# Chaper 8

# Arbitrary Keyword Arguments

# This function expects first and last name, then as many name-value 
# pairs as the user would like to pass to the function

# double asterisks creates empty dictionary that will take key-value
# pairs passed to it.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton',
                             field='physics')

print(user_profile)

# You will often see parameter name **kwargs for keyword arguments.
