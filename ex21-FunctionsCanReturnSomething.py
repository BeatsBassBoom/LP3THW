# This function adds two variables and prints a statement indicating the addition and returns the solution.
def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

# This function subtracts two variables and prints a statement indicating the subtraction and returns the solution.
def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

# This function multiplies two variables and prints a statement indicating the multiplication and returns the solution.
def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

# This function divides two variables and prints a statement indicating the division and returns the solution.
def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


# This line prints a statement indicating the start.
print("Let's do some math with just functions!")

# The next four lines set variables to specific values after calling functions to do some arthimetic passing two variables.
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# 
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")