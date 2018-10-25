# Write down every word and symbol I have used.

# we have imports for argv which adds modules to the script from libraries
from sys import argv
print()  # print statement
# = comment
+  # plus
-  # minus
/  # slash or division
*  # asterisk or multiply
%  # percent or modulo
<  # less-than
>  # greater-than
<=  # less-than-equal
>=  # greater-than-equal
=  # assign valuses to variables
print(f"{sample}")  # Print embeded variables/strings
# stores a statement with a variable in a variable for printing later if needed.
x = f"Sample print {example}"
# a way to print a statement with a variable assigned and format it, in this case with a false.
print(joke_evaluation.format(hilarious))
print(w + e)  # a way to combine two variables to be printed on one line.
# a method of printing something multiple times in this case 10 times based on the multiplier.
print("." * 10)
# sets up a template for formatting text to be printed in. e.g a space between each chracter 1 2 3 4
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))  # will print 1 2 3 4
# is the new line chracter that prints the following content on a new line of its own.
\n
print(""" """)  # Will print all the content in the format as listed if across multiple lines it will print as seen.
\\  # escapes a backslash
\'  # escapes the single quote so it prints
\"  # escapes the double quote
\a  # escape ASCII bell
\b  # escape ASCII backspace
\f  # escape ASCII formfeed
\N{name}  # Chracter named name in the Unicode database
\r  # carriage return
\t  # horizontal tab
\uxxxx  # Chracter with 16 bit hex value
\Uxxxxxxxx  # Chracter with 32 bit hex value
\v  # ASCII vertical tab
\ooo  # Chracter with octal value ooo
\xhh  # Chracter with hex value hh
input()  # prompts the user for input from the command line.
# Tells print to not end the line with a newline chracter and go to the next line.
print("Some text", end=' ')
int(input())  # takes input and converts it to a number.
pydoc  # a command that can be used to look up details of a function.
# assigns user input from the command line to variables known as unpacking.
example = argv
# specifies a variable that can be used with input() as a prompt for the user to see.
prompt = '> '
# opens the specified file for use later, can be assigned to variable.
txt = open(filename)
# calls the file opened earlier and issues the read functions to read the content of the file and print as it goes.
txt.read()
close()  # closes the file if opened, saves it
read()  # read the content of a file.
readline()  # reads one line of a textfile.
truncate()  # empties the file, aka deletes some content.
write()  # writes content to a file.
seek(0)  # moves the read/write location to the beginning of the file.


# def declares a function that takes *args meaning unlimited arguments can be applied.
def print_two(*args)


return  # returns values from a function when called.
