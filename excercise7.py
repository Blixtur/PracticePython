import sys

# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

# Creating list with contents
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Filling list with even numbers. If number in list a % 2 == 0 then that gets added to the b list.
b = [num for num in a if num % 2 == 0]

# Prints the b list
print(b)