# Excercise Verify User
# Before printing a welcome back message in greet_user(), ask the user if this is the
# correct username. If it's not, call get_new_username() to get the correct username.

import json

def get_new_username():
    filename = 'username.json'
    username = input("what is your name?")
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username



def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:  # if the attempt to retrieve a username was successful
        verify_user = input(f"Are you {username}? (y/n) ")
        if verify_user == 'y':
            print(f"Welcome back, {username}!")
            return
        if verify_user == 'n':
        # We got a username, but it's not correct.
        # Let's prompt for a new username.
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")

greet_user()



