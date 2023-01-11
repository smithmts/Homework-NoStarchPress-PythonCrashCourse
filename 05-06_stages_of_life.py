# Write an if-elif-else chain that determines a person's stage of life.
# Set value for the variable age. <2 Baby, 2-4 Toddler, 4-13 kid, 13-20
# teenager, 20-65 adult, >=65 elder.

# I'm not sure if the book is asking me to do as individual print
# statements or have if-elif-else chain populate a variable, but I'm 
# going to do the latter out of personal preference.

age = 34

if age < 2:
    stage = 'baby'
elif age < 4:
    stage = 'toddler'
elif age < 13:
    stage = 'kid'
elif age < 20:
    stage = 'teenager'
elif age < 65:
    stage = 'adult'
else:
    stage = 'elder'

# Also throwing in an if-else chain to include the appropriate use of
# "a" vs "an" in the statement.

if stage[0] in ['a','e']:
    print(f"You are an {stage}.")
else:
    print(f"You are a {stage}.")
