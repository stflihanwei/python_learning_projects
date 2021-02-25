# the input() function

message = input("I will repeat it back to you:")
print(message)

# writing clear prompts
prompt = "personalize message."
prompt += "\nWhat is your first name?"
name = input(prompt) # input () function that takes a string as parameter that will be used later
print("\nHello, " + name + "!")

# Using int() to accept numerical input
age = input("how old are you?")  # python interpret input as a string.
age = int(age)
print(age >= 18)
print(age)

# The modulo operator returns the remainder after divide
print(4%3)
print(5%3)
print(6%3)

