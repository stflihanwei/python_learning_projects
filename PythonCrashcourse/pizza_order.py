# excercise: pizza toppings. Write a loop that prompts the user to enter a series of pizza toppings
# until they enter a 'quit' value.

prompt = "\n Please order your topping: "
prompt += "\n (enter 'quit' to quit ordering)"

active = True     # have an endless loop
while active:
    topping = input(prompt)
    if topping != 'quit':
        print("\nYour topping " + topping + " is added to the pizza." )
    else:
        active = False
# or use another way

prompt = "\n Please order your topping: "
prompt += "\n (enter 'quit' to quit ordering)"

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("\nYour topping " + topping + " is added to the pizza." )
    else:
        break


