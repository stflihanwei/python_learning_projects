# The while loop in action
# while loop runs while a certain condition is true!
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nenter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)

    if message != 'quit':
        print(message)

# Using a flag
# For a program that should run only as long as many conditions are true, you can define one variable that
# determines whether or not the entire program is active.
prompt = "\nTell me something, and I will repeat it back to you:"
prompt = "\nEnter 'quit' to end the program."
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Using break to exit a loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Using continue in a loop
# count 1 - 10, only odd numbers
current_number = 0
while current_number < 10:
    current_number += 1    # current_number = current_number+1
    if current_number % 2 == 0:
        continue # return to the beginning of the loop

    print(current_number)

# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1


# Using a while loop with lists and dictionaries
# moving a list of newly registered but unverified users of a website, to a separate list of confirmed users

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()   # poping/removing users from the list and save it into a list

    print("\nVerifying user: " + current_user.title())
    confirmed_users.append(current_user)  # adding popped unconfirmed users to confirmed users
print("\nThe following users have been confirmed: ")
for confirmed_user in confirmed_users:
    print(confirmed_user)


# Removing all instances of a specific values from a list

pets = ['dog', 'cat', 'goldfish', 'cat','cat',]
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)

# Filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb?" )
    # store the response in the dictionary; accessing dictionary with name as key, and response as value
    # Dictonary[] can be used both for stroing and accessing
    responses[name] = response

    repeat = input("would you like to let another person respond? (yes/no)" )
    if repeat == 'no':
        polling_active = False

print("\n --- Polling Results ----")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")

# deli.
# loop through the list of sandwich orders and print a message for each order,
# as each sandwich is made, move it to the list of finished sandwiches.

sandwich_orders = ['Tuna sandwich', 'Eggmayonnise sandwich', 'Salmon sandwich', 'pastrami', 'pastrami',
                   'pastrami']
finished_sandwiches = []

# add a code near the beginning of your program to say deli has run out of pastrami
# use a while loop to remove all occurrences of 'pastrami' from sandwich_orders

print('We run out of pastrami.')
while 'pastrami' in pets:
    pets.remove('pastrami')
while sandwich_orders:
    sandwich_made = sandwich_orders.pop()
    print("\n I have made your " + sandwich_made)
    finished_sandwiches.append(sandwich_made)

print(finished_sandwiches)

# ask the customers to order from the sandwich list
# after the customer orderred, add it to the ordered sandwich list
# loop through the list of sandwich orders and print a message for each order,
# as each sandwich is made, move it to the list of finished sandwiches.

sandwich_menu = ['Tuna sandwich', 'Eggmayonnise sandwich', 'Salmon sandwich', 'Pastrami',]
sandwich_orders = []
finished_sandwiches = []

prompt = "\nPlease order your sandwich from the following list:" + sandwich_menu
prompt += "\nEnter 'quit' to end the program. "

while True:
    order = input(prompt)
    if message != 'quit':
        sandwich_orders.append(order)
    while sandwich_orders:
        sandwich_made = sandwich_orders.pop()
        print("\n I have made your " + sandwich_made)
        finished_sandwiches.append(sandwich_made)
    if message == 'quit':
        break
