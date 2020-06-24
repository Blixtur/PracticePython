import sys

# Make a two-player Rock-Paper-Scissors game.
# (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
# and ask if the players want to start a new game)
player1 = input("What is your name, player 1? ")
player2 = input("And what is your name, player 2?")
player1answr = input("Please take your pick. \n Rock \n Paper \n Scissors \n")
player2answr = input("Please take your pick. \n Rock \n Paper \n Scissors \n")
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

def compare(p1, p2):
    if  p1 == p2:
        return ("It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            return print("Rock wins!")
        else:
            return print("Paper wins!")
    if  p1 == p2:
        return ("It's a tie!")
    elif p1 == "rock":
        if p2 == "scissors":
            return print("Rock wins!")
        else:
            return print("Paper wins!")
    if p1 == p2:
        return print("It's a tie!")
    elif p1 == "scissors":
        if p2 == "paper":
            return print("Scissors wins!")
        else:
            return print("Paper wins!")
    elif p1 == 'scissors':
        if p2 == 'paper':
            return print("Scissors win!")
        else:
            return print("Rock wins!")
    elif p1 == 'paper':
        if p2 == 'rock':
            return print("Paper wins!")
        else:
            return print("Scissors win!")
    else:
        return print("You have not entered a valid input. The input has to be: rock, paper or scissors.")
        sys.exit()

compare(player1answr, player2answr)
sys.exit()