# Write a different version of either 07-04 or 07-05 that uses a
# conditional test in the `while` statement to stop the loop, uses an
# active variable to control how long the loop runs, and uses a break
# statement to exit the loop when the user enters a 'quit' value.

# Choosing 07-05

# Prefer setting prompt separately
prompt = "\nEnter moviegoers age"
prompt += "\nEnter 'cancel' to cancel."
prompt += "\nEnter 'finished' for your total."
prompt += "\nAge: "

active = True

total_cost = 0

while active == True:
    age = input(prompt)
    if age == 'cancel':
        break
    elif age == 'finished':
        print(f"Your total is ${total_cost}")
        active = False
    else:
        age = int(age)
        if age < 3:
            cost = "Free"
        elif age < 13:
            cost = "$10"
            total_cost += 10
        else:
            cost = "$15"
            total_cost += 15
        print(f"This ticket will be {cost}.")
