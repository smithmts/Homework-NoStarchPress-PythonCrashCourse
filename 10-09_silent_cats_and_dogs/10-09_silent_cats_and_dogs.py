filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            # Lines approach seems more appropriate since output can
            # be handled separately in the `else` block.
            lines = f.readlines()
    except FileNotFoundError:
        pass
    else:
        print(filename)
        for line in lines:
            print(f"\t{line.strip()}")
