files = ['1', '2', '3']

for file in files:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{file} not found.")
    else:
        count_1 = contents.lower().count('foo')  # word 1
        count_2 = contents.lower().count('bar')  # word 2
        count_3 = contents.count('The phrase')  # phrase

    print(count_1)
    print(count_2)
    print(count_3)
    print("...")
