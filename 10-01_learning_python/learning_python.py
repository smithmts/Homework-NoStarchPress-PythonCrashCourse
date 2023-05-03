filename = 'learning_python.txt'

# Read the entire file.
with open(filename) as file_object:
    contents = file_object.read()

print(contents)
print("...")


# Loop over a file object.
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("...")


# Store in a list and print from outside.
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
