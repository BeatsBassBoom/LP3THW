# This line assigns the number of people to a new variable
types_of_people = 10
# This line assigns a sentence with the number of people variable to a single variable
x = f"There are {types_of_people} types of people."

# This variable is assigned a string value binary
binary = "binary"
# This line assigns a string value to a variable
do_not = "don't"
# This line assigns a string value with the two variables above into a sentence inside one variable.
y = f"Those who know {binary} and those who {do_not}."

# This line prints the strings all wrapped into one with number of people
print(x)
# This line prints the combination of binary and do_not variables into one sentence.
print(y)

# This line prints the x sentence containing number of people.
print(f"I said: {x}")
# This line prints a reiteration of y continaing binary and do_not variables of those knowing.
print(f"I also said: '{y}'")

# This line assigns boolean value of false to a hilarious checker.
hilarious = False
# This line evaluates a joke based on the previous boolean variable of False.
joke_evaluation = "Isn't that joke so funny?! {}"

# This line prints the outcome of the joke evalauation as false due to the boolean value
print(joke_evaluation.format(hilarious))

# This variable assigns the beginning of a string.
w = "This is the left side of..."
# This variable assigns the end of a string 
e = "a string with a right side."

# This print statement combines both the previous variables into one sentence.
print(w + e)