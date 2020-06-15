import sys

#Requesting input from user
name = str(input("Enter your name:"))
age = int(input("Enter you age:"))

#Declaring variables and assigning a value to them
calcyear = 100 - age
yearhundred = 2020 + calcyear

#Printing the results
print("Hello, your name is", name, "and you will be 100 years old by year", yearhundred)

times = int(input("How many times would you like to have the message shown?"))
#Keeps writing lines until 'age' reaches 100.
i = 0
#Loop that allows the user to enter a desired amount of times the message will be shown.
while (i < times):
    print ("Hello, your name is", name, "and you will be 100 years old by year", yearhundred)
    i = i+1

sys.exit()