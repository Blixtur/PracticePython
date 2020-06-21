import sys

# Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

#Asks for input string
a = input("Please enter a word to check if it is a palindrome: ")
#Converts string to lowercase for comparitative reasons
a = a.lower()
#Prints string in lowercase
print (a)
#Compares string to reverse string, if true return Yes else No
if (a == a[::-1]):
    print("Yes, this is a palindrome!")
else:
    print("No, this is not a palindrome.")
#Exits the program
sys.exit()