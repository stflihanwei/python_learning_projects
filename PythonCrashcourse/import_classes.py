from car import Car # from car.py import Car class
my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()



# importing multiple classes from a module

from car import Car, Battery

my_beetle = Car('VW','beetle',2016)
print(my_beetle.get_descriptive_name())


# importing entire module

import car
my_beetle = Car('VW','beetle',2016)
print(my_beetle.get_descriptive_name())


# importing all classes from a module
# syntax: from module_name import *, not recommended.
# importing the entire module and using the module_name.class_name syntax.
# better use module_name.class_name


# importing a module into a module
# when you store your classes in several modules,
# you may find that a class in one module depends on a class in another module
# you can import the required class into the first module


from car import Car
from electric_car import ElectricCar

my_beetle = Car('VW','beetle',2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar ('tesla','roadster',2016)
print(my_tesla.get_descriptive_name())

# imported restaurant
# Using your latest restaurant class, store it in a module.
# Make a separate file that imports restaurant
# make a restaurant instance, and call one of Restaurant'' methods to show that
# the import statement is working properly.

from restaurant_class import Restaurant

my_restaurant = Restaurant('Vaniletta','Asian fusion')

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served = 2
my_restaurant.number_serve_read()
my_restaurant.increment_number_served(34)
my_restaurant.number_serve_read()

from icecreamstand_class import IcecreamStand

my_icecreamstand = IcecreamStand('Lumina')
my_icecreamstand.flavors = ['vanilla','chocolate','salmiaki']
my_icecreamstand.display_flavors()
my_icecreamstand.describe_restaurant()

#OrderedDict, if you are creating a dictionary and want to keep track of
# the order in which key-value pairs are added, you can use this.

from collections import OrderedDict
favorite_languages = OrderedDict() #create an instance of the OrderedDict class
# and store this instance in favorite_languages
# the call to OrderedDict() creates an empty ordered dictionary for us and stores
# it in favorite_languages.

# main benefit of lists(retaining your original order) with the main feature of
# dictionaries (connecting pieces of information)

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# OrderedDict Rewrite
from collections import OrderedDict

glossary = OrderedDict()

glossary['string'] = 'A series of characters.'
glossary['comment'] = 'A note in a program that the Python interpreter ignores.'
glossary['list'] = 'A collection of items in a particular order.'
glossary['loop'] = 'Work through a collection of items, one at a time.'
glossary['dictionary'] = "A collection of key-value pairs."
glossary['key'] = 'The first item in a key-value pair in a dictionary.'
glossary['value'] = 'An item associated with a key in a dictionary.'
glossary['conditional test'] = 'A comparison between two values.'
glossary['float'] = 'A numerical value with a decimal component.'
glossary['boolean expression'] = 'An expression that evaluates to True or False.'

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)


# Dice.
# the module random contains functions that generate random numbers in
# a variety of ways. The function randint() returns an integer in the range you
# provide. Make a class Die with one attribute called sides,
# which has a default value of 6.
# make a method called roll_die(). Make a 6-sided die and roll it 10 times.
# make a 10 sided die, and a 20 sided die.

from random import randint

class Die():
    def __init__(self,sides=6):
        self.sides = sides

    def roll_die(self):
        self.x = randint(1,self.sides)
        print('This  ' + str(self.sides) + '-sided dice rolled out to be '+ str(self.x))

my_dice = Die(6)
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice = Die(10)
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice = Die(20)
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()
my_dice.roll_die()

# Another way to roll a dice

from random import randint

class Die():
    """Represent a die, which can be rolled."""

    def __init__(self, sides=6):
        """Initialize the die."""
        self.sides = sides

    def roll_die(self):
        """Return a number between 1 and the number of sides."""
        return randint(1, self.sides)

# Make a 6-sided die, and show the results of 10 rolls.
d6 = Die()

results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

# Make a 10-sided die, and show the results of 10 rolls.
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print("\n10 rolls of a 10-sided die:")
print(results)

# Make a 20-sided die, and show the results of 10 rolls.
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print("\n10 rolls of a 20-sided die:")
print(results)

