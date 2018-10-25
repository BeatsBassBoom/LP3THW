# This line imports argv (arguments) from sys (system)
from sys import argv

# This line assigns the user supplied arguments into the variables from left to right.
script, user_name, age = argv
# This line assigns > as a prompt for the user to see later.
prompt = '***----*** '

# This line prints a statement displaying the user supplied arguments.
print(f"Hi {user_name}, I'm the {script} script.")
# This line asks the user to get ready for a question.
print("I'd like to ask you a few questions.")
# This line restates the user's name and asking them a question.
print(f"Do you like me {user_name}?")
# This line prompts the user to answer the question while displaying the prompt (>) from the earlier variable and stores the response in likes.
likes = input(prompt)

# This line prints a question for the user to answer while displaying the user's name again.
print(f"Where do you live {user_name}?")
# This line shows the user the prompt (>) and stores their input for the question in lives.
lives = input(prompt)

# This line prints an additional question.
print(f"What kind of computer do you have?")
# This line stores the user's input while showing them the prompt (>) in the computer variable.
computer = input(prompt)

# This line prints a paragragph formatted stated to the user showing them their answers to all the questions they were asked. (style multiline string)
print(f"""
Alright, so you said {likes} about liking me, that's very {age} of you.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")