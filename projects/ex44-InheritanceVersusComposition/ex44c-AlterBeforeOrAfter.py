# Alter Before or After


class Parent(object):
    # Alter Before or After
    # This will override the child altered.
    def altered(self):
        print("PARENT altered()")
    # Alter Before or After


class Child(Parent):
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

# Calls the respective class that calls the altered function
dad.altered()
son.altered()
