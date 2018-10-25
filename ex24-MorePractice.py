# prints a generic sentence to the user.
print("Let's practice everything.")
# a print statement that shows the escape chracter to input ' and \
print('You\'d need to know \'bout escapes with \\ that do:')
# a print statement with the escape chracter to show how to use new lines and tabs
print('\n newlines and \t tabs.')

# a variable assigned with formmatting parameters to show tabs, new lines, and """ spacing
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantation
\n\t\twhere there is none.
"""

# a trio of print statements to print the above variable with some manual formatting.
print("--------------")
print(poem)
print("--------------")

# a variable is assigned arthimetic.
five = 10 - 2 + 3 - 6
# prints the variable above within a statement.
print(f"This should be five: {five}")

# defines a formula that takes a single parameter
def secret_formula(started):
    # a trio of variables that perform multiplication, division
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    # returns the three calculations to the function call.
    return jelly_beans, jars, crates

# assigns a value to a variable
start_point = 10000
# three variables get the return value from the function called with the parameter start_point.
beans, jars, crates = secret_formula(start_point)

# prints a statement with the variable output at the end thanks to the format function
# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# print statement for printing the variable returned from the above function call on line 40
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# assigns a variable with arthmetic
start_point = start_point / 10

# Simple print statement
print("We can also do that this way:")
# variable is assigned the returned value from the function call.
formula = secret_formula(start_point)
# This formatted print allows all three of the assigned variables in formula to be printed out individually with the {}
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))