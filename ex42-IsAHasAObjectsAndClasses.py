'''
1. Research why Python added this strange object class and what that means.
    Python added object classes to better group data and functionality together. Classes create new objects which allow new instances of the class to be created. Python classes are based on C to provide features of OOP. That means a single class can have as many object instances as needed.

2. Is it possible to use a class like it’s an object?
    Yes, because a class is a class is a class based on Python. Classes can be referenced directly or as arguments example: super(Employee, self).__init__(name).

3. Fill out the animals, fish, and people in this exercise with functions that make them do things. See
what happens when functions are in a ”base class” like Animal versus in, say, Dog.

4. Find other people’s code and work out all the is-a and has-a relationships.

5. Make some new relationships that are lists and dictionaries so you can also have ”has-many”
relationships.

6. Do you think there’s such thing as an ”is-many” relationship? Read about ”multiple inheritance,”
then avoid it if you can.
    Yes and it seems pointless and clunky and repetitive. Multiple inheritance is when a class can be derived from multiple base classes. The features of all the base classes are inherited into the derived class. Meaning Base1 and Base2 would go into the derived class MultiDerived.
'''

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal.
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name.
        self.name = name
    def walk(self, pace):
        ## Dog has-a pace
        self.pace = pace

## Cat is-a Animal.
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name.
        self.name = name
    def pounce(self, jump):
        ## Cat has-a jump.
        self.jump = jump
    def body(self):
        ## Cat has-a body has-many legs
        self.legs = {}

## Person is-a object.
class Person(object):

    def __init__(self, name):
        ## Person has-a name.
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None
    def body(self, weight):
        ## Person has-a body has-a weight.
        self.weight = weight
    def hand(self):
        ## Person has-a hand has-many fingers.
        self.fingers = [] 


## Employee is-a Person.
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        ## Employee has-a name.
        # This is how to run the __init__ method of a parent class reliably.
        super(Employee, self).__init__(name)
        ## Employee has-a salary.
        self.salary = salary

## Fish is-a object.
class Fish(object):
    pass

## Salmon is-a Fish.
class Salmon(Fish):
    pass

## Halibut is-a Fish.
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat.
satan = Cat("Satan")

## mary is-a Person.
mary = Person("Mary")

## mary has-a pet satan
mary.pet = satan

## frank is-a Employee.
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon.
crouse = Salmon()

## harry is-a Halibut.
harry = Halibut()