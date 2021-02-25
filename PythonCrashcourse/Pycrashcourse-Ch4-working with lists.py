# Doing more work within a for loop
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("Good job," + magician.title() + ".\n")

# Using range() to make a list of numbers
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)

# more concisely
squares = []
for square in range(1,11):
    squares.append(square**2) # append function can only be used for lists
print(squares)

# list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)


# Simple statistics with a list of Numbers
digits = [1,2,3,4,5,6,7,8,9]
min(digits)
max(digits)
sum(digits)

# summing a million: make a list of one million, use min() and max() and sum()
number = []
for value in range(1,1000001):
    number.append(value)
print(max(number))
print(min(number))
print(sum(number))
print(number[len(number)-1])

# Threes, make a list of multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.
threes = []
for number in range(1,10):
    threes.append(number*3)
print(threes)

# Cubes: Make a list of the first 10 cubes 1 to 10, print out the value of each cube
cube = []
for number in range (1,10):
    cube.append(number**3)
print(cube)

# list comprehension
cube = [number**3 for number in range(1,10)]
print(cube)

# slicing a list
players = ['charles','martina','michael','florence']
print(players[0:3])
print(players[:3])
print(players[2:])
print(players[-3:]) # negative index returns an element a certain distance from the end of a list: last three players

# looping through a slice
print("\nHere are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# Copying a list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]  # copying a list without connecting them together like my_foods = friend_foods
friend_foods.append('ice cream')
my_foods.append('cannoli')
print(friend_foods)
print(my_foods)

# tuples unchangeable list
dimensions = (200,50)
print(dimensions[1])

# writing over a tuple
dimensions = (200,50)
print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
