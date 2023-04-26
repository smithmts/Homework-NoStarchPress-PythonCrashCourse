# Prompt
Go to [Python Module of the Week](https://pymotw.com/), and review a module listed in the table of contents, perhaps `random`

# Selection
Went with [random](https://pymotw.com/3/random/index.html) per the suggestion.

# Observations
- Pseudorandom, as suspected.
- Looks like I should have been using `uniform` method from the module instead of random, since I am specifying a range? Actually, `random` is floating point and I was using `randint` to obtain integers.
- Side, note, I got the desired result from my use of `range`, but it looks like I could have just used (6) instead of (0,6)?
- Looks like I can use `seed` method to first establish a set of random numbers, and then select future randomized results from that seed.
- Looks like `shuffle` method would force unique values; however, the I don't totally understand everything going on in the example, so I'm only like 70% certain.
- Look to other functions for normal distributions and other applications; don't under-think it and just use random.
