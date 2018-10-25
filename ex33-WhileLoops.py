# declares loop start value
i = 0
# declares empty list variable
numbers = []

# declares the while loop to stop at 6
while i < 6:
    print(f"At the top i is {i}")
    # appends the current place to the end of numbers list
    numbers.append(i)

    # increases the loop place each time around.
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")
# Prints all the numbers in the list via loop
for num in numbers:
    print(num)