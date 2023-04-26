from admin_priv_classes import Admin
# The class we are calling directly is `Admin` so we go to that module
# and import that class.

user_7 = Admin('Alfred', 'Acronym', 'aacronym', 'aa@owca.net', 'USA')
user_7.privileges.show_privileges()
