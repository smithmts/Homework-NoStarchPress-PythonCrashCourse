# Poll users about dream vacation.
# Write a prompt simliar to "If you could visit one place in the world,
# where would you go?
# Include a block of code that prints the results of the poll.

# Filling a Dictionary with User Input
responses = {}

# Setting a prompt to avoid the line going long.
place_prompt = "If you could go anywhere in the world, "
place_prompt += "where would you go? "

# Set active flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Propmt for name and response.
    name = input("\nWhat is your name? ")
    response = input(place_prompt)
    # Store the response in the dictionary
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete.  Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to {response}.")
