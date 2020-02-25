#THESE ARE MY NOTES AND CODES FOR MY FIRST OPP
#This is an animals by it's age
animals = [('leon', 5), ('cat',1)]
# Classes are used to create new user-defined data structures that contain arbitrary information about something
# It’s important to note that a class just provides structure—it’s a blueprint or a
# template for how something should be defined, but it doesn’t actually provide any real content itself.

class Animals:
    pass
#All classes create objects, and all objects contain characteristics called attributes
class Dogs:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# While instance attributes are specific to each object, class attributes are the same for all instances—which in this case is all dogs
class Dogs:
#Class attribute
    species = 'Mammals'
    def __init__(self, name, age):
        self.name = name
        self.age = age
#Instantiating is a fancy term for creating a new, unique instance of a class.
a = Dogs('pepe', 1)
b = Dogs('tesla', 3)
print (a == b) #False

# More complex example:
# Instantiate the Dog object
philo = Dogs("Phile", 5)
mikey = Dogs("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}".format(philo.name, philo.age, mikey.name, mikey.age))
#Is philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(philo.name, philo.species))

def get_biggest_number(*args):
    biggest = 0
    for arg in args:
        if arg > biggest:
            biggest = arg
            #or you can just do biggest = max(args)
    print(f'The biggest is {biggest}')

a = Dogs('pepe', 1)
b = Dogs('tesla', 2)
c = Dogs('MrP', 5)
get_biggest_number(a.age, b.age, c.age)

#Class attribute
species = 'mammal'
#Initializer / Instance Attributes
def __init__(self, name, age):
    self.name = name
    self.age = age

#Instance method
    def description(self):
        return"{} is {} years old".format(self.anem,self.age)
    #instance method
    def speak(self, sound):
        return "{} says {}".forat(self.name, sound)
# Instantiate the Dog object
mikey = Dogs("Mikey", 6)

# call our isntace methods
print(mikey.description())
print(mikey.speak("Gruff Gruff"))
# MODIFYING ATTRIBUTES
#You can change the value of attributes based on some behavior:

class Dogs:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #Instance method
    def birthday(self):
        self.age +=1
#Instiate the Dog object
mikey = Dogs("Mikey", 6)
#call our instance methods
mikey.birthday()
#If we want to differenciate one dog from another we can use Dog's breeds
#For instance:

class Dog:
    def __instancecheck__(self, breed):
        self.breed = breed
    spenser = Dog("Terrier")
    spenser.breed
    sara = Dog('German Sheperd')
    sara.breed
#Creating seperate classes for each breed (These are child classes of the parent Dog class.)
# Parent class
class Dogs:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        return"{} is {} years old".format(self.anem,self.age)
    def speak(self, sound):
        return "{} says {}".forat(self.name, sound)
    #Child classes
class RusselTerrier(Dogs)
    def run(self , speed):
        return "{} runs {}".format(self.name, speed)
class Bulldog(Dogs):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)
#Now entering the behaviors (attributes)
jim = Bulldog("Jim", 12)
print(jim.description())
#Now to specify
print(jim.run("slowly"))

