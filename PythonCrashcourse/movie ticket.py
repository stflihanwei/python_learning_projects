# Movie tickets: if person under 3, the ticket is free. if they are between 3 and 12, the ticket is $10;
# if they are over age 12, the ticket is $15. Write a loop in which you ask users their age,
# then tell them the cost of their movie ticket.

prompt = "\n What is your age? "
prompt += "\n (enter 'quit' to quit ticket booking.)"

active = True

while active:  # flag variable. or while True:
    age = input(prompt)
    if age == 'quit':
        active = False  # neither this line or next line alone works
        break
    try:
        age = int(age)
    except ValueError:    # try: except ValueError: have python handle error if the enter is not what is expected
        continue
    if age != 'quit':
        if age < 3:
            print("Your ticket is free.")
        if age >= 3 and age <= 12:
            print("Your ticket is $10.")
        if age > 12:
            print("Your ticket is $15.")
    else:
        break

# use a conditional test in the while statement
# use an active variable to control how long the loop runs

