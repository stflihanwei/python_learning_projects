class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):  # the parameter are only
        # used in init function
        self.name = restaurant_name  # self.nameofnewvariable (instance variable)=parameter of init function
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name.title())
        print("It is a " + self.cuisine.title() + " type restaurant.")

    def open_restaurant(self):
        print("The restaurant " + self.name.title() + " is now open!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def number_serve_read(self):
        print(str(str(self.number_served) + " tables have been served already."))

    def increment_number_served(self, increase_number):
        self.number_served += increase_number
        # original table number served + increase number

