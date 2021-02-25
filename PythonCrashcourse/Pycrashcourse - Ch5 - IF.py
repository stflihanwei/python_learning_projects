# Conditional tests: checking for equality
car = 'BMW'
print(car == 'bmw')
print(car == 'audi')

# testing for equality is case sensitive
print(car == 'BMW')
print(car.lower() == 'bmw')
print(car)

# Checking for inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

answer = 17
if answer != 42:
    print("Wrong answer!")

# checking multiple conditions and or
age_0 = 22
age_1 = 22
print(age_0 >= 21 and age_1 >=21)
print(age_0 >=21 or age_1>= 21)

# Checking whether a value is in a list
print('mushroom' in requested_topping)

# Checking whether a value in a list
banned_users = ['andrew', 'carolina','david']
users = ['marie', 'andrew']

if users[0] not in banned_users:
    print(users[0].title() + ", you can post.")
if users[1] in banned_users:
    print(users[1].title() + ", Fuck off!")


thing = 'woohoo'
print ("Is thing == 'have sex'? I predict true")
print(thing == 'have sex')

# the if-elif-else chain, only appropriate to use when you just need one test to pass
# admission for under 4 free, between 4 and 18 $5, above 18 $10
age = 4
if age < 4:
    price = 0
elif age < 18:  # if the above conditions are not met
    price = 5
else:          # if no other condition is met, default condition
    price = 10

print("Your admission is $" + str(price))

# If you need two conditions met, you need two if statement
requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms'in requested_topping:
    print("Adding mushrooms")
if 'extra cheese' in requested_topping:
    print ("Adding extra cheese")   # using second if this line of command execute regarless of previous one

pizza_topping = ''
for topping in requested_topping:
    pizza_topping = pizza_topping + ' ' + topping

print("Your pizza will be with" + pizza_topping + ".")

# python short-hand: ' '.join(list_name)
print("Your pizza will be with " + ', '.join(requested_topping))


# Hello Admin   'dfsdf','sdfwe','rge','admin','erwerio'
username_list = []

if not username_list:           # empty list is boolean false, if not convert to boolean true. if list is empty
    print('We need to find some users!')

for username in username_list:
    if username == 'admin':
        print('Hello admin, would you like to see status report?')
    else:
        print('Hello ' + username + ", thank you for logging in today.")

print(bool([]))
print(bool([1]))
print(bool(''))
print(bool('1'))
print(bool(0))
print(bool(1))

# find repetitive username
current_users = ['dfsdf','sdfwe','rge','admin','erwerio']
new_users = ['kfigod','dkdkdk','ewfefvd','dkfiw','admin']

# two loops
for user in new_users:
    for used_name in current_users:
        if user == used_name:
            found = True
            print ('Find a new username.')
        else:            # else always need to come after if. since else is in the second loop,
            # result will be printed 5*5
            print ('This username is available')

# introducing boolean variable

for user in new_users:
    found = False
    for used_name in current_users:
        if user == used_name:
            found = True
            print ('Find a new username.')
    if not found:              # if not means if which only accept negative boolean condition
        print ('This username is available')

# short-hand
for user in new_users:
    if user in current_users:
        print('\nFind a new username')
    else:
        print('\nThis username is available')

# ordinal numbers
number_list = [1,2,3,4,5,6,7,8,9]
for number in number_list:
    if number == 1:
        print(str(number) + 'st')
    elif number == 2:
        print(str(number) + 'nd')
    elif number == 3:
        print(str(number) + 'rd')
    else:
        print(str(number) + 'th')
