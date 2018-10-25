# This line imports the argv features (modules) from sys (system) source
from sys import argv
# read the WYSS section for how to run this
# This line assigns the arguments supplied by the user to the variables starting from the left broken by a space in the script execution.
script, first, second, third = argv

# This line prints the variables with the arguments supplied by the user.
print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)


script = input("Input script name: ")
first = input("Input first: ")
second = input("Input second: ")
third = input("Input third: ")