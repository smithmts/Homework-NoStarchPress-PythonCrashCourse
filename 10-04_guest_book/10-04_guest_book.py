# Write a `while` loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a
# line recording their visit in a file called guest_book.txt

filename = 'guest_book.txt'
active = True

with open(filename, 'w') as file_object:
    while active:
        response = input("Please enter your name (enter q to quit): ")
        if response == 'q':
            print("All names have been recorded to the guest book.")
            active = False
        else:
            print(f"Hello {response.title()}!")
            file_object.write(f"{response}\n")
