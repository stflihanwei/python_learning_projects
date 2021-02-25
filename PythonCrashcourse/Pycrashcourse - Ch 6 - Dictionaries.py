# [] list () access list {} dictionary [] access dictionary () tuple

# A simple dictionary: different kinds of information about one object
# starting with an empty dictionary
alien_0 = {}
alien_0 = {'color': {'aa': 123}, 'points': 12}  # key value pairs
print(alien_0['color'])  # accessing key values
print(alien_0['points'])


alien_1 = {'birth': {'month': 12, 'date':10}, 'genetics': [4251, 5421]}  # you can put a dictionary inside a key
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")

# adding new key-value pairs to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Modifying values in a dictionary

alien_0['color'] = {'yellow'}

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium', 'point': 1}

print('Original x_position:' + str(alien_0['x_position']))

# move the alien to the right
# determine how far to move the alien based on its current speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
x = 'x_position'  # you can put the dictionary key in a variable
print(alien_0[x])

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

alien_0['speed'] = 'fast'
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position:" + str(alien_0['x_position']))

# Removing key-value pairs

del alien_0['point']
print(alien_0)

# A dictionary of similar objects: use a dictionary to store one kind of information about many objects

favourite_languages = {
    'jen': 'python',
    'john': 'c',
}

print("Jen's favourite language is " + favourite_languages['jen'].title() + ".")

favourite_number = {
    'jen': 1,
    'jane': 2,
}

# looping through all key-value pairs

user_0 = {
    'username':'fsdf',
    'first': 'fermi',
}

for key, value in user_0.items():   # need to create names for the two variables
    print("\nKey:" + key)
    print("Value:" + value)

for name, language in favourite_languages.items():   # The first variable refer to key, second to value
    print(name.title() + "'s favourite language is " + language.title() + ".")

# Looping through all the keys in a Dictionary
# .keys() when you don't need to work with all the values in a dictionary
for name in favourite_languages.keys():
    print(name.title())
# or = the same result
for name in favourite_languages:
    print(name.title())

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll!")

# looping through a dictionary's keys in order:
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping through all values in a dictionary
for language in favourite_languages.values():
    print(language.title())

# show values without repetition:
for language in set(favourite_languages.values()):
    print(language.title())

# Rivers make a dictionary of river and country.


rivers = {
    'nile':'egypt',
    'Danube':'Austria',
    'Yellow rive':'China',
    'Heng': 'India',
          }

# loop to print a sentence about each river, such as the Nile runs through Egypt.
for river, country in sorted(rivers.items()):
    print ("The " + river + " runs through " + country + ".")

# use a loop to print the name of each river included in the dictionary
for river in rivers:
    print(river)


# use a loop to print all the key value set in dictionary
for names in rivers.items():
    print(names)

# use a loop to print the name of each country included in the dictionary
for country in rivers.values():
    print(country)

# use code in favourite languages. make a list of people who should take the poll.
name_list = ['jen', 'john','Ingrid', 'Hanwei', 'Mauri']

favourite_languages = {
    'jen': 'python',
    'john': 'c',
}

for name in name_list:
    if name in favourite_languages.keys():
        print("Hi " + name.title() + ", I see your favourite language is " + favourite_languages[name].title()
              + ", thank you for taking the poll.")
    else:
        print("Hi " + name + ", please take the poll!")

# Nesting
# make an empty list for storing alients.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color':'green', 'points':5, 'speed':'slow'}
    aliens.append(new_alien)
print(new_alien)

# show the first 5 aliens. show a list of dictionaries.
for alien in aliens[:5]:
    print(alien)
print("...")

# show how many aliens have been created.
print("Total number of aliens:" + str(len(aliens)))

# change some aliens
for alien in aliens[0:5]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
print()
for alien in aliens[:30]:
    print("This is a alien" + str(alien))

# A list in a dictionary
# store information about a pizza being ordered
pizza = {
    'crust' : 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

print("You ordered a " + pizza ['crust'] + "-crust pizza " + "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)

favourite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c', 'go']
}

for name, languages in favourite_languages.items():
    print(name.title() + "'s favourite languages are:")
    for language in languages:
        print("\t" + language.title())

# A dictionary in a dictionary
users = {
    'aeinstein':{
        'first': 'albert',
        'last': 'einstein',
        'location':'princeton',
    },
    'mcurie':{
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    }

}

for username, user_info in users.items(): # key stores in username, 
    print("\nUsername:" + username)
    full_name = user_info['first'] + " " + user_info['last']     # variable_name[key name] - access a key
    location = user_info['location']

    print("\tFull name:" + full_name.title())
    print("\tLocation:" + location.title())


# Excercise. Make several dictionairies, the name of each dictionary is the name of a pet.
# In each dictionary, include the kind of animal and the owner'' name.
# store these dictionaries in a list called pets.
# Loop through your list and as you do print everything you know about each pet.

pets = {
    'aron': {
        'kind': 'dog',
        'breed': 'labrador',
        'owner': 'james',
    },

    'lizz': {
        'kind': 'cat',
        'breed': 'prusian',
        'owner': 'jane',
    }
}

for pet_name, pet_info in pets.items():
    print("\nPet name:" + pet_name.title())
    pet_kind = pet_info['kind'].title() +' '+ pet_info['breed'].title()
    pet_owner = pet_info['owner'].title()

    print("\n Pet information:")
    print("\t Pet kind:" + pet_kind)
    print("\t Pet owner:" + pet_owner)


# Favourite places
# make a dictionary called favorite_places, think of three names to use as keys in the dictionary
# to make this excercise a bit more interesting, ask some friends to name a few of their favorite places
# loop through dictionary, and print each person's name and their favorite places



# cities
# make a dictionary called cities, use the name of three cities as keys in your dictionary.
# approximate population, one fact about that city, the keys: country, population, fact

cities = {
    'SanFrancisco': {
        'country':'USA',
        'population': 100000,
        'fact':'lots of hills'
    },
    'Geneva': {
        'country': 'Switzerland',
        'population': 100000,
        'fact': 'lakes and swans'
    },

}

for city_name, city_info in cities.items():
    print("\nCity name: " + city_name.title())
    city_basicinfo = 'This city is in ' + city_info['country'] + '. It has population of ' + str(city_info['population'])
    city_moreinfo = 'This city has '+ city_info['fact']

    print("\n City information:")
    print("\t City basic information:" + city_basicinfo)
    print("\t City more information:" + city_moreinfo)



