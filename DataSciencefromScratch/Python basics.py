# List comprehension
even_numbers = [x for x in range(5) if x%2 ==0]  # why put an x in front of the for?
print(even_numbers)

squares = [x* x for x in range(5)] # range (5) is 0 1 2 3 4
print(squares)

even_squares = [x*x for x in even_numbers]
print(even_squares)

# turn list into dictionaries
square_dict = {x: x*x for x in range(5)}
print(square_dict)

square_set = {x*x for x in [1,-1]}
print(square_set)

list = [x*x for x in range(2)]
print(list)

# if you don't need the value from the list, it'' conventional to use an underscore as the variable
zeroes = [0 for _ in even_numbers] # What does this mean?
print(zeroes)

# A list comprehension can include multiple fors:

pairs = [(x,y)
         for x in range(10)
         for y in range(x+1,10)]  # only pairs with x<y
print(pairs)


# Well also you can use longer version that looks like this:

def generate_evens():
    result = []
    for x in range(1, 50):
        if x % 2 == 0:
            result.append(x)
    return result
print(generate_evens())

# This is a shorter version
def generate_evens1():
    return [x for x in range(1, 50) if x % 2 == 0]

print (generate_evens1())

# Generators and iterators

def natural_numbers():
    n = 1
    while True:
        yield n
        n += 1

natural_numbers()

lazy_evens_below_20 = (i for i in range(20) if i % 2 ==0)


import random

#random.random() produces numbers uniformly between 0 and 1, it'' the random function we''l use most often
four_uniform_random = [random.random() for _ in range(4)]

# you can set random.seed if you want to get reproducible results:
# if you set the same number for seed, the random number sequence will be the same.
# if you want random number, you set the seed on other things, such as time stamp
random.seed(10)
print(random.random())
print(random.random())
random.seed(10)
print(random.random())
print(random.random())
print(random.random())
print(random.random())
random.seed(10)
print(random.random())
print(random.random())
print(random.random())
print(random.random())
print(random.random())

# fibonaci sequence

def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)


# use random.randrange, takes either 1 or 2 arguments

print(random.randrange(10)) # choose randomly from range(10) = [1,2,...,9]
print(random.randrange(3,6,2)) # choose randomly from range (3,6) = [3,4,5]

# random.shuffle randomly reorders the elements of a list
up_to_ten = [x for x in range(10) if x%2 ==0]
random.shuffle(up_to_ten)
print(up_to_ten)

# randomly pick one element from a list random.choice
friend = random.choice(["alice", "bob","charlie"])

# randomly choose a sample of elements without replacement
lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers,6)

# choose a sample of elements with replacement, make multiple calls to random.choice.
four_with_replacement = [random.choice(range(10))
                         for _ in range(4)]









