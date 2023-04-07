from pizza import make_pizza as mp
# Using an alias use to reference the function thrroughout this
# program.
# could alias the module, for example `import pizza as p`

# Now use the function contained in pizza
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

# At least in my testing, specific function import requires omitting 
# 'pizza.'
