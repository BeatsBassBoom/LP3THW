# This line imports argv (arguments) so the user can be prompted to input arguments on the command line.
from sys import argv

# These assignments take arguments from the user on the command line and stores them in the variables from left to right.
script, filename = argv

# Assigns the contents of the filename supplied by the user in the txt variable by using the open funtion which is given the filename variable storing the argument given by the user.
txt = open(filename)

# Prints the filename the user entered on the command line for them to see.
print(f"Here's your file {filename}:")
# This reads the text from the file stored in the txt variable by calling the read function with no parameters that read to the eof.
print(txt.read())

# prints a statement asking the user to input the same filename again.
print("Type the filename again:")
# Supplies a prompt for the user to enter the filename again that will be stored in a different variable this time.
file_again = input("> ")

# This line opens the file the user supplied a second time and stores it in the new text again variable by calling the open function and supplying the new file name variable.
txt_again = open(file_again)

# This line calls the read function for the text stored in the variable text again from the file again and then prints them line by 
print(txt_again.read())


### I still need to learn how to use the close function.