# Implicit Inheritance


class Parent(object):
    # Implicit Inheritance
    def implicit(self):
        # Will override child
        print("PARENT implicit()\n")


class Child(Parent):
    pass


# Assigns the dad variable equal to the Parent class
dad = Parent()
# Assigns the son variable equal to the Child class
son = Child()

# Calls the respective class that calls the implicit function
dad.implicit()
son.implicit()
