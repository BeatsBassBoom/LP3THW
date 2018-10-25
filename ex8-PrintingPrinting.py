# This line creates a function for formatting with {} which I do not fully understand just yet.
formatter = "{} {} {} {}"

# This line prints the numbers with the formatter function called from line 1
print(formatter.format(1,2,3,4))
# This line also prints a specifice format from line 1 for the strings below
print(formatter.format("one", "two", "three", "four"))
# This line prints the boolean values in the line 1 format.
print(formatter.format(True, False, False, True))
# This line prints the function created on line 1 formatter printing all of its actual contents {}
print(formatter.format(formatter, formatter, formatter, formatter))
# This line prints the strings on one line in the format designated in the formatter function as a string sentence.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))