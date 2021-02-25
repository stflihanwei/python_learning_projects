# ask the customers to order from the sandwich list
# after the customer orderred, add it to the ordered sandwich list
# loop through the list of sandwich orders and print a message for each order,
# as each sandwich is made, move it to the list of finished sandwiches.

sandwich_menu = ['tuna', 'eggmayonnise', 'salmon', 'pastrami']
finished_sandwiches = []


prompt = "\nPlease order your sandwich from the following list:"
prompt += str(sandwich_menu)
prompt += "\nEnter 'quit' to end the program. "

while True:
    order = input(prompt)
    if order != 'quit':
        sandwich_order = order.lower()
        if sandwich_order not in sandwich_menu:
            print("We don't have this sandwich. Please order from menu!")
        else:
            print("\n I have made your " + sandwich_order)
            finished_sandwiches.append(sandwich_order)
            print(sandwich_order)
            print(finished_sandwiches)
    if order == 'quit':
        break
