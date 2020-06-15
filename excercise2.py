import sys
# Ask the user for a number.
# Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

x = int(input("Please enter a number: "))
if x % 4 == 0:
    print("This is a multiple of 4")
elif x % 2 == 0:
    print("This number is an even number")
else:
    print ("This is an un-even number")

num = int(input("Please enter a number to check: "))
check = int(input("Enter the number to divide by: "))
if num % check == 0:
    print("This is an even number.")
else:
    print("This is an un-even number.")


sys.exit()
