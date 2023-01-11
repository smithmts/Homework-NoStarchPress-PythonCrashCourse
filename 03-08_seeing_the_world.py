places = ['Banff', 'England', 'Vancouver', 'Victoria', 'New York']
print(places)

#Use Sorted
print("Temp Sort:")
print(sorted(places))

#show original again
print("See, still not permanently sorted:")
print(places)

#Reverse sort
print("Reverse Sorted:")
print(sorted(places, reverse=True))

#show original again.
print("See, still not permanently sorted:")
print(places)

#Reverse permanently
places.reverse()
print("Now permanently reversed:")
print(places)

#Reverse again
places.reverse()
print("Now permanently reversed the other way:")
print(places)

#Permanently sort alpha
places.sort()
print("Permanently sorted alphabetically now:")
print(places)

#Permanently sort reverse alpha
places.sort(reverse=True)
print("Permanently sorted reverse alpha now:")
print(places)

# Using len (using this list instead of going back to dinner guests
# sinces it's on my phone.
print("The number of items in the list is: ", len(places))
