# This line prints a question to the user on one line
print("How old are you? ", end='')
# This variable stores the user's input into a variable
age=input()
print("How tall are you? ", end='')
height = input()
print("How much do you weigh? ", end='')
weight = input()

# This line prints all the variables the user's inputer was stored in.
print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("Why do you need this?", end='')
reason = input()

print(f"So you know what you are doing that's why you need to print {reason}")