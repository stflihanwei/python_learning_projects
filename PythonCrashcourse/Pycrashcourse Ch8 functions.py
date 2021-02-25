# Defining a function
def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()

# Passing information to a function

def greet_user(username):
    """ Display a simple greeting."""
    print("Hello, " +username.title() + "!")
greet_user('jesse')
greet_user('mauri')
greet_user('hanwei')

# Message write a function called display_message() that prints one sentence telling everyone what you are
# learning in this chapter. Call the function, and make sure the message displays correctly.

username = [1,2,3,4,5,6,7,8,9,10,]
def display_message(username):
    print(username)
display_message(username)

# write a function called favorite_book() that accepts one parameter, title. Print a message, such as one of
# my favorite book is ....

def favorite_book(title):
    print("My favorite book is " + title)
favorite_book('The pale blue dot')

# Passing argument
# Positional arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('hamster', 'harry')

# Multiple function calls. You can call a function as much times as you need.
def describe_pet(animal_type, pet_name):
    """Display information about"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster','harry')
describe_pet('dog', 'willie')

# Order matters in positional arguments
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('harry', 'hamster')

# Keyword arguments
# the way of defining a function is the same for positional & keyword argument
# the difference is when you call the function, that you associate the name and value within the argument
# so when you pass the argument to the function, there is no confusion.
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet(animal_type= 'hamster', pet_name='harry')

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type = 'dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'' name is " + pet_name.title() + ".")
describe_pet(pet_name = 'willie')

# Equivalent Function calls
def describe_pet(pet_name, animal_type = 'dog'):
    describe_pet('willie')
    describe_pet(pet_name='willie')

    describe_pet('harry', 'hamster')
    describe_pet(pet_name='harry', animal_type='hamster')
    describe_pet(animal_type='hamster', pet_name='harry')

# Avoiding argument errors
def describe_pet(animal_type, pet_name):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('labrado', 'Maomao')

# T-shirt
# write a function called make_shirt() that accepts a size and the text of a message that should be printed
# The function should print a sentence summarizing the size of the shirt

def make_shirt(size = 'M', shirt_message = 'live your life'):
    print("Your shirt will be size " + size + ", with message printed on front: " + shirt_message)

make_shirt('S')

# Cities
def describe_city(city_name,country):
    print(city_name + " is in " + country)

describe_city('Helsinki','Finland')

# other ways

def describe_city(city_name,country):
    return city_name + country

print(describe_city('Helsinki','Finland'))



# Return
# a function doesn't always have to display its output directly. Instead it can process some data
# and then return a value or set of values.
# The return statement takes a value from inside a function and then send it back to the line that called
# function


# A simple value
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()    # return value is a output
musician = get_formatted_name('jimi', 'hendrix')
print(musician)  #function is self-contained. So you have to give a name to the new variable.
print(get_formatted_name('jimi', 'matrix')) #get the same result, python give a temporary variable for it


# Making an argument optional

def get_formatted_name (first_name,last_name,middle_name=''): # middle_name is optional, listed last,
# and default value is an empty string
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# or
musician = get_formatted_name('lang','lang')
print(musician)

# Returning a dictionary
def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)


# dictionary with optional value
def build_person(first_name, last_name, age = ''): # age is a optional variable
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'hendrix', age= 27)
print(musician)

# using a function with a while loop
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("Enter 'q' to exit")
    f_name = input("First name:")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")


# City names.  write a function called city_country() that takes in the name of a city and its country.
def city_names(city,country):
    print(city.title() + ' ' + country.title())


city_names('santiago','chile')
city_names('beijing','china')  # call function using string ''


# Passing a list
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print("\n" + msg)

usernames = ['hannah', 'ty', 'margot']  # define a list
greet_users(usernames)   # pass a list of names to this function

# modifying a list in a function

# start with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# simulate printing each design, until none are left
# move each design to completed_models after printing.

while unprinted_designs:
    current_design = unprinted_designs.pop()   # pop() function to remove and store printing designs

# simulate creating a 3D print from the design.
    print("Printing model:" + current_design)
    completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# rewriting the previous code using function. So next time doing the same procedure you don't
# need to copy paste the same code over again.

def print_models(unprinted_designs, completed_models):   # Every function should have one specific job
    """
    simulate printing each design, until none are left. Move each design to completed_models after print)
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)


# Preventing a function from modifying a list
# In case you want to keep the original list of unprinted designs for your records.
# function_name(list_name[:]) when you call the function

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
new_designs = []

# if you call a function like this it will modify the original list unprinted_design

# a function needs to be  self-contain, so it should not contain an outside list

def copy_models(copy_designs, append_item):
    copy_list = copy_designs[:]       # if you use: copy_list = copy_designs,
    # the append will change the original and new list, that's why you need to copy list [:]
    copy_list.append(append_item)
    return copy_list       # need to have a return function to be assigned a new variable

new_designs = copy_models(unprinted_designs,'aaa')

print(new_designs)
print(unprinted_designs)

# however, this will change the original list and new list,
# because they are only pointing to the same list

def copy_models(copy_designs,append_item):
    copy_model = copy_designs
    copy_designs.append(append_item)
    return copy_model

new_designs = copy_models(unprinted_designs, 'aaa')

print(new_designs)
print(unprinted_designs)

# print_models(unprinted_designs[:], completed_models)

# magicians

magician = ['hanwei', 'mauri']

def show_magicians(magician_name):
    print(magician_name)
    return magician_name     # after return function, the function exit

show_magicians(magician)

# great magicians. make a copy of your program. modifies the list by adding the phrase the Great to
# each magician's name

def make_great(magician_name):
    magicians = magician_name[:]
    make_great_magician = []   # the empty list need to be outside of loop,
    # because if it is inside the loop, it will be overwritten!!!
    for magician in magicians:
        make_great = 'the Great ' + magician
        make_great_magician.append(make_great)
    print(make_great_magician)
    return make_great_magician

make_great(magician)



def make_great(magician_name):
    magicians = magician_name[:]
    for magician in magicians:
        make_great = 'the Great ' + magician
        print(make_great)
    return make_great

make_great(magician)
show_magicians(magician)


# Passing an arbitrary number of arguments
def make_pizza(*toppings):  # * in the parameter, pass many arguments into the parameter (instead of one normally)
# the result will always be a tuple, not a list
# cannot take keyword argument make_pizza(toppings='pepperoni')
    """print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')
make_pizza('pepperoni','mushrooms','green peppers','extra cheese')

# change into a loop

def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms','green peppers','extra cheese')


# mixing positional and arbitrary arguments

# if you want a function to accept several different kinds of arguments, the parameter that accepts
# an arbitrary number of arguments must be placed last in the function definition.
def make_pizza(size, *toppings):
    print("\nMaking a " +str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'mushroom')


# Using arbitrary keyword arguments
def build_profile(first, last,**user_info):
    profile = {}
    profile['first_name'] = first  # storing value: first into key:'first_name'
    profile['last_name'] = last
    for key, value in user_info.items(): #using .items() to loop through key and value in dictionary
        profile[key] = value
    return profile

user_profile = build_profile('Hanwei', 'Li', location = 'tampere', field = 'sociology')

print(user_profile)

# sandwiches.
# write a function that accepts a list of items a person wants on a sandwich. accept as many items
# print a summary of the sandwich.

def sandwich_order(*ingredients):
    print('Making a sandwich with:')
    print(ingredients)

sandwich_order('cheese','tuna','red herring')

# user profile
def user_profile(first_name,last_name,**user_info):
    profile = {}
    profile['first name'] = first_name
    profile['last name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    print(profile)
    return profile

user_profile('Hanwei', 'Li', location = 'Tampere',occupation = 'Researcher')

# cars
def make_car(manufacturer, model, **other_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in other_info.items():
        car[key] = value
    print(car)
    return car

car = make_car('nissan','range roger',color='blue', tow_package = True)



# import an entire module: module_name.py
# module_name.function_name()


import make_pizza    # imported the make_pizza file as a module

make_pizza.make_pizza(16, 'pepperoni')   # using make_pizza module and using make_pizza function
make_pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')



# importing specific functions

# from module_name import function_name

# from module_name import function_0, function_1, function_2

# using as to give a function an alias

from make_pizza import make_pizza as mp

mp(16,'pepperoni')
mp(12, 'mushrooms','green peppers', 'extra cheese')

# from module_name import function_name as fn

# use as to give a module an alias

import make_pizza as mp
mp.make_pizza(16,'pepperoni')

# importing all functions in a module

from make_pizza import *

make_pizza(16,'pepperoni')




