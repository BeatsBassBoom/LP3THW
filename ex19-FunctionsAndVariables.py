# this line defines my function to take two parameters.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # This print statement prints the parameters passed in by the function calls.
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

# This print statement prints a line to the user.
print("We can just give the function numbers directly:")
# Calls the function at the top to print all the statements with the two values supplied.
cheese_and_crackers(20, 30)

# This line prints a statement to the user.
print("OR, we can use variables from our script:")
# This line sets the variable to 10
amount_of_cheese = 10
# This line sets the variable to 50
amount_of_crackers = 50

# This line calls the function above passing variables containing integers instead of ints directly.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This line prints a statement to the user.
print("We can even do math inside too:")
# Calls the function at the top with ints that are calculated with addition before actually passing them to the function to print them out to the user.
cheese_and_crackers(10 + 20, 5 + 6)

# Prints a statemetn to the user before doing math with the variables.
print("And we can combine the two, variables and math:")
# Calls the function above with variables that are calculated with math addition ints and actual variables containing ints.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)