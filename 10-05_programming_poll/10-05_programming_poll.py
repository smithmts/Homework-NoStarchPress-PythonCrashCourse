# Write a `while` loop that asks people while they like programming.
# Each time someone enters a reason, add their reason to a file that
# stores all the responses.

# It doesn't really specify, but I am going to use append mode for
# this exercise.

filename = 'programming_poll.txt'
prompt = "What is a reason you like programming? (q to quit): "
active = True

while active:
    response = input(prompt)
    if response == 'q':
        print("All of your reasons have been recorded.")
        active = False
    else:
        with open(filename, 'a') as file_object:
            file_object.write(f"{response}\n")
        print(f"Your response ({response}) has been recorded.")
