# bring your functions in modules
# you can go a step further by storing your functions in a separate file called module, and then
# importing that module into your main program.

# import an entire module


def make_pizza(size,*toppings):
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

