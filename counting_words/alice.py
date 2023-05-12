# Chapter 10

# `try-except` block for FeileNotFoundError

filename = 'alice.txt'

# 'f' is a common variable assignment for file objects.
# Demonstrates encoding option, which is needed when the system's
# default does not match that of the file being read.
try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
