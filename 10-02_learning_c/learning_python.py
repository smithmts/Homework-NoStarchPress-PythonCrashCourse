filename = 'learning_python.txt'

# Chose `for line` approach since it seems the most concise
with open(filename) as file_object:
    for line in file_object:
        print(line.strip().replace('Python', 'C').replace('.', '?'))
        # I'm only 95% positive that all three of my things learned
        # are also true in C, so decided to try a multiple replace.
        # chaining `replace()` was what my gut said to try, and Stack
        # Overflow seems to confirm it is the fastest.
