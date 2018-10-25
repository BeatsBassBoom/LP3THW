# Imports sys modules argv (arguments) features
from sys import argv

# stores user input from the command line in two variables via arguments import.
script, input_file = argv

# function setup for printing all lines taking a single parameter.
def print_all(f):
    # prints each line in the file supplied via the f parameter.
    print(f.read())

# function setup for replaying the lines already printed.
def rewind(f):
    # call to seek feature, not sure of all features, but recalls the lines printed.
    f.seek(0)

# function setup for printing a specific line receiving two parameters for line count and the file.
def print_a_line(line_count, f):
    # prints the line count number for each line while printing the content with the readline function for the file.
    print(line_count, f.readline())

# assigns the file the user supplies to a new variable after the open function is used to open it for use.
current_file = open(input_file)

# prints a standard external comment to the user with a new line underneath.
print("First let's print the whole file:\n")

# calls the function print all passing it the current file that opened the input file.
print_all(current_file)

# prints a standard external comment to the user.
print("\nNow let's rewind, kind of like a tape.")

# calls the reqind function with the parameter of the current file.
rewind(current_file)

# prints a standard external comment to the user.
print("\nLet's print three lines:")

# sets the current line count at 1
current_line = 1
# calls the function print a line with the current line count and the current file that was opened for reading.
print_a_line(current_line, current_file)

# increases the current line count by one
current_line += 1
# calls the print a line function with two parameters to print additional lines from the file.
print_a_line(current_line, current_file)

# increases the current line count by 1
current_line += 1
# calls print a line function with the increased count and current file parameters.
print_a_line(current_line, current_file)