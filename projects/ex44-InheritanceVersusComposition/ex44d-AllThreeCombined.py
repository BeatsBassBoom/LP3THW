# All Three Combined

"""
Inheritance or Composition:
1. Avoid multiple inheritance at all costs, as it’s too complex to be reliable. If you’re stuck with it,
then be prepared to know the class hierarchy and spend time finding where everything is coming
from.

2. Use composition to package code into modules that are used in many different unrelated places
and situations.

3. Use inheritance only when there are clearly related reusable pieces of code that fit under a single
common concept or if you have to because of something you’re using.

"""


class Parent(object):

    # Override Explicitly
    # Prints statement below and will override the child.
    def override(self):
        print("Parent override()\n")

    # Implicit Inheritance
    def implicit(self):
        # Will override child
        print("PARENT implicit()\n")

    # Alter Before or After
    # This will override the child altered.
    def altered(self):
        print("PARENT altered()")


class Child(Parent):

    # Override Explicitly - this function overrides the Parent
    def override(self):
        # This line will be overriden by the parent.
        print("CHILD override()\n")

    # Alter Before or After
    def altered(self):
        # This print statement overrides the parent altered function.
        print("CHILD, BEFORE PARENT altered()")
        # This line overrides the child state to run the parent altered function.
        # Handles all of the method resolution order
        super(Child, self).altered()
        # This line overrides the parent function to print the child statement.
        print("CHILD, AFTER PARENT altered()\n")


# Assigns the dad variable equal to the Parent class
dad = Parent()
# Assigns the son variable equal to the Child class
son = Child()

# Calls the respective class that calls the implicit function
dad.implicit()
son.implicit()

# Calls the respective class that calls the override function
dad.override()
son.override()

# Calls the respective class that calls the altered function
dad.altered()
son.altered()

'''
class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        # super() with __init__ example - same as son.altered()
        super(Child, self).__init__()
'''
