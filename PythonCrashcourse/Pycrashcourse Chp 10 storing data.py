# Storing data
# json module allows you to dump simple python data structures into a file and load the data
# from that file the next time the program runs. You can also use json to share data between
# different python programs.


import json

numbers = [2,3,4,5,6,7]

filename = 'numbers.json'
with open(filename, 'w') as f_obj: # open the file in write mode
    json.dump(numbers,f_obj) # use the json.dump() function to
    # store the list numbers in the file numbers.json

    # the list of numbers is stored in numbers.json file


# read the list back into memory

import json

numbers = [2,3,4,5,6,7]

filename = 'numbers.json'
with open(filename) as f_obj: # open the file in read mode
    numbers = json.load(f_obj)

print(numbers)

# Saving and reading user-generated Data

import json

username = input("what is your name?")

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username,f_obj)   # use json.dump() function to pass it a username and
    # a file object, to store the username in a file
    print("we'll remember you when you come back, " + username + "!")

# a program that greets a user whose name has been stored

import json

filename = 'username.json'

with open(filename) as f_obj:
    username = json.load(f_obj)
    print("Welcome back, " + username + "!")

# combine two programs together into one file

import json

# Refactoring
# you can improve the code by breaking it up into a series of functions that have specific jobs


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("what is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
       username = get_stored_username()
       if username:
           print("Welcome back, " + username + "!")
       else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()


# favourite number

import json

filename = 'favourite_number.json'

def favourite_number():
    favourite_number = input('What is your favourite number?')
    with open(filename,'w') as f:
        json.dump(favourite_number,f)
        print("Your favourite number " + favourite_number + " is stored.")

def show_favourite_number():
    try:
        with open(filename) as f_obj:
            show_number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        print("I know your favourite number is " + show_number)


favourite_number()
show_favourite_number()


# Excercise Verify User

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("what is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
       username = get_stored_username()
       if username:
           print("Welcome back, " + username + "!")
       else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")

greet_user()


