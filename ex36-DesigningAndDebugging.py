'''
HOMEWORK
Now write a game similar to the one that I created in the last exercise. It can be any kind of game you want in the same flavor. Spend a week on it making it as interesting as possible. For Study Drills, use lists, functions, and modules (remember those from Exercise 13?) as much as possible, and find as many new pieces of Python as you can to make the game work.

Before you start coding you must draw a map for your game. Create the rooms, monsters, and traps that the player must go through on paper before you code.

Once you have your map, try to code it up. If you find problems with the map then adjust it and make the code match.

The best way to work on a piece of software is in small chunks like this:

1. On a sheet of paper or an index card, write a list of tasks you need to complete to finish the software. This is your to-do list.

2. Pick the easiest thing you can do from your list.

3. Write out English comments in your source file as a guide for how you would accomplish this task in your code.

4. Write some of the code under the English comments.

5. Quickly run your script so see if that code worked.

6. Keep working in a cycle of writing some code, running it to test it, and fixing it until it works.

7. Cross this task off your list, then pick your next easiest task and repeat.

This process will help you work on software in a methodical and consistent manner. As you work, update your list by removing tasks you don’t really need and adding ones you do
'''


# function for checking if the office is open
def is_office_open():
    # ask the user what time it is and save it
    print("What time is it currently in 24 hour format hours only e.g. 14?")
    time = int(input("> "))

    if time >= 8 and time <= 18:
        print("Yes the office is open!")
        tobacco_smell_checker()
    else:
        print("The office is closed right now, please try reporting later.")
        exit()

# function for tobacco smell checker in my house
def tobacco_smell_checker():
    print("Do you smell smoke in my house?")
    tobacco_smell = input(">>> ")

    if tobacco_smell == "Yes":
        print("We are going to check if your evil neighbor is on their balcony now. . .")
        evil_neighbor_on_balcony()
    elif tobacco_smell == "No":
        print("No smoking is a good thing, come back if you smell tobacco.")
        exit()
    else:
        print("You failed to enter Yes or No, let's try again.\n")
        tobacco_smell_checker()

# function to check for evil neighbor smoking
def evil_neighbor_on_balcony():
    print("Take a look out your sliding doors, do you see your neighbor?")
    neighbor_on_balcony = input(">> ")

    if neighbor_on_balcony == "Yes":
        print("\nLooks like there is visual confirmation of smoking by you.")
        print("We are now alerting the office!")
        alert_office_of_smoking(neighbor_on_balcony)
    elif neighbor_on_balcony == "No":
        print("\nNot on the balcony, doesn't mean they are guilty.")
        print("The office is being contacted, they will go out and take a look anyway.")
        alert_office_of_smoking(neighbor_on_balcony)
    else:
        print("\nYou did not enter a proper answer, let's try again (e.g Yes or No)")
        evil_neighbor_on_balcony()

# Function for alerting the office of smoking in my house if true
def alert_office_of_smoking(status_of_neighbor):

    if status_of_neighbor == "Yes":
        print("We have been alerted of smoking in your area with visual proof from you.")
    elif status_of_neighbor == "No":
        print("Your neighbor may not be on the balcony smoking, someone is going outside to check.")
    else:
        print("Thanks for contacting the front office.")


is_office_open()