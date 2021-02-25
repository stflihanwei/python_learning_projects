from restaurant_class import Restaurant
class IcecreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type = 'icecream'):
        # even if you keep it like def __init__(self): the first position will be
        #restaurant_name and the second position will be cuisine_type
        super().__init__(restaurant_name,'icecream',) # initialize attributes of the parent class
        # super() function helps python make connections between the parent and child
        # you can either repeat the parent class attributes name here, or pass a
        # new positional argument to the cuisine_type
        # in this case, the cuisine_type = icecream
        # or cuisine_type = 'icecream'
        # but in any case, you will need to have two attributes there
        # you can only use the ones from parent init function, cannot add additional one
        self.flavors = []  # when you want the users to pass the flavors to the list
        self.restaurant_name = restaurant_name

    def display_flavors (self):
        print("\nThis " + self.restaurant_name +
              " restaurant has the following flavors available:")
        for flavor in self.flavors:  # when do you have to use self.xxx
            print("- " + flavor.title())  # when you don't have to use self.xx
