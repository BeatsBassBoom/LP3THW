# bringing in the exit library from system module
from sys import exit

# method creation for a room with gold
def gold_room():
    # ask the user to make a choice.
    print("This room is full of gold. How much do you take?")

    # store the user's choice in a variable
    choice = input("> ")
    # check for values and store in new variable if true.
    if "0" in choice or "1" in choice:
        # store the checked choice in the variable.
        how_much = int(choice)
    # if choice not 1 or 0 notify of wrong choice.
    else:
        dead("Man, learn to type a number.")

    # check choice for threshold, print statement based on amount.
    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        # exit if the the user's choice is under 50.
        exit(0)
    else:
        dead("You greedy bastard!")

# method to creat a room with a bear.
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    # set the default position of the bear not moved.
    bear_moved = False

    # create an endless loop until the user wins.
    while True:
        # store the user's choice.
        choice = input("> ")

        # check what choice the user made.
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taught bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taught bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")

# method for facing a new set of choices.
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    # take user input.
    choice = input("> ")

    # action based on a user's choice.
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

# method to tell the user why they are dead and exit the program.
def dead(why):
    print(why, "Good job!")
    exit(0)

# Initiate the game.
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around th room until you starve.")

# call to start the game.
start()