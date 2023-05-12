# Chapter 10

# Analyzing text.

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split()  # All words into list.
    num_words = len(words)  # Count objects in that list.
    print(f"The file {filename} has about {num_words} words.")
