# Reading from a file
with open('''pi_digits.txt''') as file_object:
    # the open() function needs one argument: the name of the file
    # python looks for this file in the directory where the program currently
    # being executed is stored. open() function returns an object representing the
    # file.python stores this objet in file_object,
    # which we will work with later in the program
    # keyword with closes the file once access to it is no longer needed.
    # you can open and close the file by calling open() and close()
    contents = file_object.read()
    # use the read() method in the second line to read the entire contents of
    # the file and store it as one long string in contents
    print(contents.rstrip())
    # rstrip() method removes any whitespace characters from the right side of
    # a string

# File paths
# with open('text_files/filename.txt') as file_object:   linux and OSX
# with open('text_files\filename.txt') as file_object:    Windows
# you can also tell python where the file exactly is.

file_path = '/PythonCrashcourse/pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# Reading line by line

filename = 'pi_digits.txt'


with open(filename) as file_object:
    # call open(), an object representing the file and its contents is stored
    # in the variable file_object
    for line in file_object:
        print(line.rstrip())

# Making a list of lines from a file

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # readline() method takes each line from the file and stores it in a list

# build a single string containing all the digits in the file with no white space
# in it.
pi_string = ''
for line in lines:
    pi_string += line.strip()

# Large files, one million digits.
print(pi_string[:52] + "...")
print('\n' + line.rstrip())

# when python reads from a text file, it interprets all text in the file as a string.
# if you read ina number, and want to work with that value in a numerical context.
# convert it to a integer using int(), or a float using float()


# is your birthday contained in Pi?

filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # readline() method takes each line from the file and stores it in a list

# build a single string containing all the digits in the file with no white space
# in it.
pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = "enter your birthday, in mmddyy:"
if birthday in pi_string:
    print("Your birthday appears in pi")
else:
    print("your birthday does not appear in pi")

# Excercise learning Python
# write a program that reads the file and prints what you wrote three times.
# print the contents once by reading in the entire file, once by looping over the file object,
# and


# reading through entire file

with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    print(contents.rstrip())
    print(contents.rstrip())


file_path = '/PythonCrashcourse/learning_python.txt'

with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# line by line.
with open(filename) as file_object:
    # call open(), an object representing the file and its contents is stored
    # in the variable file_object
    for line in file_object:
        print(line.rstrip())

filename = 'learning_python.txt'
with open(filename) as f_obj:
    lines = f_obj.readlines()
for line in lines:
    print(line.rstrip())

# Once by storing the lines in a list and then working with them outside the with block

filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
    # readline() method takes each line from the file and stores it in a list

# build a single string containing all the digits in the file with no white space
# in it.
pi_string = ''
for line in lines:
    pi_string += line.strip()

# standard answer

filename = 'learning_python.txt'

print("--- Reading in the entire file:")
with open(filename) as f:
    contents = f.read()
print(contents)

print("\n--- Looping over the lines:")
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print("\n--- Storing the lines in a list:")
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

# message

guest = "\nI really like dogs."
print(guest.replace('dog', 'cat'))

# Read in each line from the file you just created, learning_python.txt, and
# replace the word Python with the name of another language, such as C.
# Print each modified line to the screen.

print("your answer:")

with open(filename) as f:
    for line in f:
        line = line.rstrip()
        print(line.replace('Python','C'))  # pay attention to the capital letters when you use
        # the replace  function.

filename = 'learning_python.txt'
print('standard answer:')
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    line = line.rstrip()
    print(line.replace('Python', 'C'))

# use rstrip() and replace () on the same line

filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:
    # Get rid of newline, then replace Python with C.
    print(line.rstrip().replace('Python', 'C'))

# writing to a file

# writing to an empty file

filename = 'programming.txt'

with open(filename,'w') as file_object: # we want to open the file in the write mode 'w'
    # you can open in read mode 'r', write mode 'w', append mode 'a' or read and write 'r+'
    # if you omit, it opens in ready-only mode by default
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')

# python can only write strings to a text file, use str() to write numerical data

# Appending to a file

with open(filename,'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run ina browser.\n")

# guest

filename = 'guest_list.txt'
prompt = "\nWhat is your name dear guest?"
prompt += "\nenter 'q' to end the program. "
guest = ""
while guest != 'q':
    guest = input(prompt)
    print("Welcome, dear " + guest.title())
    with open(filename, 'a') as file_object:
        file_object.write(f"{guest.title()}\n")
        print(f"Hi {guest}, you have been added to the guest book.")
    if guest != 'q':
        print(guest)


# Programming Poll

file = 'programming_poll.txt'

responses = []

while True:
    response = input("Why do you like programming?")
    responses.append(response)

    continue_poll = input("Would you like to let someone else respond? (y/n) ")
    if continue_poll != 'y':
        break

with open(file,'a') as f:
    f.write(f"{responses}\n")


# Exceptions
# try-except block

try:
    print(5/0)
except ZeroDivisionError:
    print("You can'' divide by zero!")

# the else block

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

while True:
    first_number = input("\nFirst number:")
    if first_number == 'q':
        break
    second_number = input('Second number:')
    if second_number == 'q':
        break
    try:
        answer = int(first_number)/int(second_number)
    except ZeroDivisionError:
        print("You can'' divide by 0!")
    except ValueError:
        print("Please enter a number.")
    else:
        print(answer)

# handling the FileNotFoundError Exception.

filename = 'alice.txt'
try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + 'does not exist.'
    print(msg)
else:
    words = contents.split()
    num_words = len(words)
    print("The file " + filename + "has about " + str(num_words) + "words.")


# Analyzing Text

title = 'Alice in Wonderland'
title.split()

# split() method separates a string into parts wherever it finds a space and stores
# all the parts of the string in a list. The result is a list of words from the string,
# although some punctuation may also appear with some of the words.


# Working with multiple files
# using a function

filename = 'alice.txt'
def count_words(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry, the file ' + filename + 'does not exist.'
        print(msg)
        # Failing silently, use:
        # pass
        # pass also acts as a placeholder. we can write any missing filenames to a file called
        # missing_filex.txt. Users wouldn't see this file, but we'' be able to read the file and deal
        # with any missing texts. how do you do that?
    else:
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) + "words.")

filename = 'alice.txt'
count_words(filename)

filenames = ['alice.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)


# Excercise Addition

print("\n Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit")

prompt1 = "\n Please give the first number:"
prompt2 = "\n Please give the second number:"

addition = []

while True:
    first_number = input(prompt1)
    if first_number == 'q':
        break
    second_number = input(prompt2)
    if second_number == 'q':
        break
    try:
        addition = int(first_number) + int(second_number)
    except ValueError:
        print("You have to enter a number.")
    else:
        print(addition)

# Standard answer

print("Enter 'q' at any time to quit.\n")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("Give me another number: ")
        if y == 'q':
            break

        y = int(y)

    except ValueError:
        print("Sorry, I really needed a number.")

    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")


# Cats and dogs
try:
    with open('cats.txt') as cats:
        contents_cats = cats.read()
        print(f"\nReading file: cats.txt")
        print(contents_cats)

    with open('dogs.txt') as dogs:
        contents_dogs = dogs.read()
        print(f"\nReading file: dogs.txt")
        print(contents_dogs)
except FileNotFoundError:
    print('This file you are looking for is missing.')

# standard answer:
filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print("  Sorry, I can't find that file.")
        # pass (silent fail)

# Excercise common words

line = "Row, row, row your boat"
line.count('row')
line.lower().count('row')

filename = 'alice.txt'

contents = ""

try:
    with open(filename) as f:
        contents = f.read()
except FileNotFoundError:
    pass
else:
    wordcount = contents.lower.count('the')
    msg = f"'the' appears in {filename} for {wordcount} times."



