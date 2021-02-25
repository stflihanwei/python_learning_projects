#Try it yourself
"""
Store the names of a few of your friens ina list called names.
Print each person'' name by accessing each element in the list, one at a time.
"""

names = ["Hanwei","Mauri","Gaoming","Tanyu"]
print(names[1])
print(names[1])

#Make a programme, ask the person's name. Then answer, Hanwei loves name.

# Greetings. print each person'' name, print a message to them.
# The text of each message should be the same, but each message should be personalized with
# the person's name.

message = "Hanwei loves " + names[1]
print(message)

message_1 = "I would like to harvest " + names[1] + "!"
print(message_1)

#3-4 Guest list: Make a list that includes who you want to invite?
# Then use list to print a invitation message to each of them to dinner.

guest = ["Carl Sagen", "Albert Einstein", "Deng xiaoping"]

invitation_message = "Dear " + guest[0] + ": " \
                                         "\nHanwei would like to invite you to a dinner. Please RSVP!" \
                                         "\nThank you!" \
                                         "\nYours sincerely, " \
                                         "\nHanwei"
print(invitation_message)

#how to repeat until every guest name is included in the print list.
for person in guest:
    invitation_message = "Dear " + person + ": " \
                                              "\nHanwei would like to invite you to a dinner. Please RSVP!" \
                                              "\nThank you!" \
                                              "\nYours sincerely, " \
                                              "\nHanwei"
    print(invitation_message)

# 3-5 changing guest list
guest_notcoming = ["Deng xiaoping"]
message_3 = "Some guest cannot make it, which is " + guest_notcoming[0] + "."
print(message_3)

guest[2] = "Lee kwan yaw"
print(guest)
for person in guest:
    invitation_message = "Dear " + person + ": " \
                                              "\nHanwei would like to invite you to a dinner. Please RSVP!" \
                                              "\nThank you!" \
                                              "\nYours sincerely, " \
                                              "\nHanwei"
    print(invitation_message)
# You just found a bigger dinner table, so now more space is available.
# Think of three more guests to invite to dinner.
# Use insert() to add one new guest to the beginning, middle, and append() to the end of your list
guest.append('Mauri Mustonen')   # instance of list class
guest.insert(0,'Bill Bryson')
guest.insert(2,'Bill Gates')
guest.insert(3,'Warren Buffet')


print(guest)

# You just you only have space for two guests.
# Use pop() to remove guests from your list one at a time, until only two.
# when remove, print a message to that person.
# pop() removes the last item in a list, but it lets you work with that item after removing it.

guest = ['Bill Bryson', 'Carl Sagen', 'Bill Gates', 'Warren Buffet', 'Albert Einstein', 'Lee kwan yaw', 'Mauri Mustonen']

print(len(guest))
print(range(len(guest)))

for i in range(len(guest)):
    print(len(guest))
    if len(guest) < 3:
        break
    popped_guest = guest.pop()
    cancel_message = "Dear " + popped_guest + ": " \
                                                  "\nSorry, the dinner is cancelled!" \
                                                  "\nYours sincerely, " \
                                                  "\nHanwei"
    print(cancel_message)
    print(len(guest))

# use del to remove the last two names from the list
del guest[0]
print(guest)

#sort() a list permanently
guest = ['Bill Bryson', 'Carl Sagen', 'Bill Gates', 'Warren Buffet', 'Albert Einstein', 'Lee kwan yaw', 'Mauri Mustonen']
guest.sort()
print(guest)

# sort reverse alphabetical order
guest.sort(reverse=True)
print(guest)

#sorted() sort a list temporarily
print("Here is the original guest list:")
print(guest)

print("\nHere is the Sorted list:")
print(sorted(guest))

# print list in reversed order permanently, use reverse() same list again to revert to original order
print("Here is the original guest list:")
print(guest)
guest.reverse()
print("\nHere is the reversed list")
print(guest)

# access last item in a list use the index -1
print(guest[-1])


