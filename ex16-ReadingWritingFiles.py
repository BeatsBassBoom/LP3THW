# This line import the argv module from the sys package
from sys import argv

# This line takes arguments on the command line when the script is called and assigns the strings to the two variables from left to right.
script, filename = argv

# This prints a statement to the user with the filename they enter on the command line call for the pyton file.
print(f"We're going to erase {filename}.")
# Prints the statement to the user to hit control c to close the app.
print("If you don't want that, hit CTRL-C(^C).")
# Prints the statement to the user to hit enter to continue the program.
print("If you do want that, hit RETURN.")

# Shows the user a ? prompt then waits for their response to the two above statements. 
input("?")

# Lets the user know the file is now being opened.
print("Opening the file...")
# This is the call to open the filename supplied by the user for writing to and stores that file in target to be over wrote. Sets up the filename as a new target file that will be written to replace the original file supplied by the user. The w supplied opens the file for writing explicitly to truncate the file but does not actually do it so the truncate call is needed later.
target = open(filename, 'w')

# Gives the user the message to let them know the file is now being over wrote.
print("Truncating the file. Goodbye!")
# Calls the truncate function to empty the files contents, completly removes all current content in the file.
target.truncate()

# Prints a statement to the user letting them know to get ready for three new lines.
print("Now I'm going to ask you for three lines.")

# Prompts the user to input strings on the first line and stores it in line1 variable, and so on.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

# Prints the statement to the user letting them know the lines will now be written to the filename supplied.
print("I'm going to write these to the file.")

# The target file is used to call the write function and supplies the line variable to each line. It writes that line to the target file on a new line for each line.
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# Lets the user know we are done and will be closing the target file parameter.
print("And finally, we close it.")
# The actual function call to close to close the target file.
target.close()