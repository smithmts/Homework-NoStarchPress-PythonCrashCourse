# Make a list of the first 10 cubes (cube of each interger from 1 to 
# 10) and use a for loop to print out the value of each cube.
cubes = []
for value in range(1,11):
    cube = value **3
    cubes.append(cube)
print(cubes)
