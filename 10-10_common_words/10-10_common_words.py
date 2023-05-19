files = ['dracula.txt', 'romeo_and_juliet.txt',
         'the_picture_of_dorian_gray.txt']

for file in files:
    try:
        with open(file) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"{file} not found.")
    else:
        count_of = contents.lower().count(' of ')
        count_to = contents.lower().count(' to ')
        count_should_have = contents.count(' should have ')

    print(file)
    print(f"\tCount of word 'of': {count_of}")
    print(f"\tCount of word 'to': {count_to}")
    print(f"\tCount of phrase 'should have': {count_should_have}")
