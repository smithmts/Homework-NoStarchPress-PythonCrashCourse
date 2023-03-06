# Chapter 7

# Filling a Dictionary with User Input
responses = {}

# Set active flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Propmt for name and response.
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain would you like to climb someday? ")
    # Store the response in the dictionary
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete.  Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
