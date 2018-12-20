import random


# Function to roll dice and set the point 6 and under
def set_dice_limits():
    for number in range(1):
        minimum_dice = random.randint(1, 6)
        maximum_dice = random.randint(1, 6)
    return minimum_dice, maximum_dice


# Call to set dice and store the point.
def roll_two_dice():
    die_one, die_two = set_dice_limits()
    maintain_point(die_one, die_two)
    print(die_one, die_two)


# Check if gamer is a winner or loser on first roll of dice
def maintain_point(die_one, die_two):
    set_point = die_one + die_two
    if set_point in {7, 11}:
        print("winner! You get to roll again.")
    elif set_point in {2, 3, 12}:
        print("You lose, new roller!")
    else:
        print(f"Match point not hit any winners with {die_one}, {die_two}")


# Prompt the user to roll dice again.
def roll_again():
    play_again = input("Would you like to roll again? (Y)es or (N)o? ")
    if play_again in {"Y", "Yes", "yes"}:
        roll_two_dice()
    elif play_again in {"N", "No", "no"}:
        print("Thanks for playing!")
        exit()
    else:
        print("You failed to enter a correct response, please try again!")
        roll_again()


# Not yet implemented but will keep track of roll count.
def check_if_first_roll():
    pass
