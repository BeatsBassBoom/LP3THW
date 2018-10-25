ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

# Splt the list ten things on a single space.
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]


while len(stuff) != 10:
    # Pop one item off the more_stuff list from the last value
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    # Append next_one to the end of stuff.
    stuff.append(next_one)
    # prints the length of stuff one item at a time through the list.
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # whoa! fancy
print(stuff.pop())
# Join the list into one line seperating each item by a space.
print(' '.join(stuff)) # what? cool!
# Takes elements 3 to 4 not 5. 
print('#'.join(stuff[3:5])) # super stellar!