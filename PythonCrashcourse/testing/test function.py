unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
new_designs = []

# if you call a function like this it will modify the original list unprinted_design

# a function needs to be  self-contain, so it should not contain an outside list

def copy_models(copy_designs, append_item):
    copy_list = copy_designs[:]       # if you use: copy_list = copy_designs,
    # the append will change the original and new list, that's why you need to copy list [:]
    copy_list.append(append_item)
    return copy_list       # need to have a return function to be assigned a new variable

new_designs = copy_models(unprinted_designs,'aaa')

print(new_designs)
print(unprinted_designs)

# however, this will change the original list and new list,
# because they are only pointing to the same list

def copy_models(copy_designs,append_item):
    copy_model = copy_designs
    copy_designs.append(append_item)
    return copy_model

new_designs = copy_models(unprinted_designs, 'aaa')

print(new_designs)
print(unprinted_designs)



#test = unprinted_designs
#test = unprinted_designs[:]
#test.append('hanwei')
#copy_models(unprinted_designs[:])
#print(unprinted_designs)
