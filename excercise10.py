import sys
import random
# Returns a list that contains only the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# *** Below is imported from my previous solution to excercise 5 ***

# Creating two sets of lists. a and b
a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
randomlista = set(random.sample(range(1, 100), 25))
randomlistb = set(random.sample(range(1, 100), 25))
# Creating lists for matching values
matchinglist = []
matchingrandomlist = []

# Appending matching values to lists
matchinglist.append(a.intersection((b)))
matchingrandomlist.append(randomlista.intersection((randomlistb)))

# Printing the matching parts of the above a and b list
print(matchinglist)
# Printing the matching parts of the above randomlista and randomlistb
print(matchingrandomlist)

sys.exit()