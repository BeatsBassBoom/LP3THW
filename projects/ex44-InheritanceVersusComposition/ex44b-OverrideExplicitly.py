# Override Explictly


class Parent(object):

    # Override Explicitly
    # Prints statement below and will override the child.
    def override(self):
        print("PARENT override()\n")


class Child(Parent):

    # Override Explicitly - this function overrides the Parent
    def override(self):
        # This line will be overriden by the parent.
        print("CHILD override()\n")


# Assigns the dad variable equal to the Parent class
dad = Parent()
# Assigns the son variable equal to the Child class
son = Child()

# Calls the respective class that calls the override function
dad.override()
son.override()
