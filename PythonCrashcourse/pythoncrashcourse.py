Name = "Eric"
print("Hello " + Name + ", would you like to learn some Python today?")

famous_person = "Albert Einstein"
print(famous_person + ' once said, A person who never made a mistake never tried anything new."')

name = " Hanwei "
print(name.title())
print(name.strip())
print("\nname")

fruit = ['apple', 'pear', 'banana', 'avocado', 'dragonfruit', 'pineapple']
fish = ('salmon', 'makerelli', 'kuha')
print(fruit)
del fruit[3]
print(fruit)
popped_fruit = fruit.pop()
print(fruit)
print(popped_fruit)

favourite_fruit = fruit.pop()
print('My favourite fruit is ' + favourite_fruit.title() + '.')

fruit = ['apple', 'pear', 'banana', 'avocado', 'dragonfruit', 'pineapple','apple','apple']
fruit.remove('banana')
print(fruit)
too_expensive = 'apple'
print(too_expensive)
fruit.remove(too_expensive)
print(fruit)

for index, fruit_x in enumerate(fruit):
    print(index)
    for fruit_y in fruit[index+1]:
        if fruit_y == fruit_x:
            print(fruit_y)
            fruit.remove(fruit_y)
print(fruit)

#how to remove repetitive word in a list?
numbers =[5,2,1,7,5,4]
numbers.sort()
for index, value_x in enumerate(numbers):
    for value_y in numbers[index+1:]:
        if value_y == value_x:
            print(value_y)
            numbers.remove(value_y)
print(numbers)



