import sys
import random


#Generate a random number between 1 and 9 (including 1 and 9).
#Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

#Keep track of how many guesses the user has taken, and when the game ends, print this out.
tries = 0
randnum = random.randint(1, 9)
print(randnum)
keepgoing = 5
while keepgoing == 5:
    tries = tries + 1
    user_guess = int(input("Please enter a number between 1 to 9 in order to guess \n"))
    print(user_guess)
    if randnum == user_guess:
        print("Correct!")
        print("It took", tries, "guesses to get the right answer!")
        sys.exit()
    elif randnum < user_guess:
        print("Too high!")
    elif randnum > user_guess:
        print("Too low!")
    elif randnum != (1, 10):
        sys.exit()

