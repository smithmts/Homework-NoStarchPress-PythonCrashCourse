# As the user their age, then tell them the cost of their ticket.
# Under 3: Free
# 3-12: $10
# >12: $15

# Prefer setting prompt separately
prompt = "Enter your age: "

age = input(prompt)
age = int(age)

if age < 3:
    cost = "Free"
elif age < 13:
    cost = "$10"
else:
    cost = "$15"

print(f"Your ticket will be {cost}.")
