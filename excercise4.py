import sys
# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


divisive_number = int(input("Enter a number, you will get the divisive number as feedback: "))

divisor = list(range(1,divisive_number+1))
divisorlist = []

for number in divisor:
    if divisive_number % number == 0:
        divisorlist.append(number)

print(divisorlist)
sys.exit()

# % == 0