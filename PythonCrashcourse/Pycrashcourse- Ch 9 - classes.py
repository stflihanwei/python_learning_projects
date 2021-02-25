# Creating and using a class
# Creating the dog class

# Classes contain characteristics called Attributes.
# We make a distinction between instance attributes and class attributes.
#
# Instance Attributes are unique to each object,
# (an instance is another name for an object).
# Here, any Dog object we create will be able to store its name and age.
# We can change either attribute of either dog, without affecting any other dog
# objects we’ve created.

# Class Attributes are unique to each class.
# Each instance of the class will have this attribute.
# It’s sometimes used to specify a default value that all objects should have
# after they’ve been instantiated. Here, our class attribute is species


class Dog():
    def __init__(self, name, age):  # make it the first function python run automatically
        # based on the dog class, it will return a new instance.
        # User always have to pass values to the init function parameter/argument
        # when creating a new instance of this Class! REQUIRED!
        # self is passed automatically, it's the same for every function inside a class,
        # no exception
        species = 'mammal'
        self.name = name  # define an instance variable/attribute from the name parameter
        # within dog class init function
        # because the name parameter is only available within the init function, not outside
        # to use name parameter, you have to use self.name in other functions.

        self.age = age

    def sit(self): # some functions does not take any paramter. Therefore when you use it
        # the () is empty
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        print(self.name.title() + " rolled over!")


# Making an new instance from the dog class
my_dog = Dog('willie', 6)

print("My dog'' name is " + my_dog.name.title() + ".")  # accessing attributes
# of an instance: my_dog.name
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()  # calling methods, methods are functions within classes
my_dog.roll_over()

your_dog = Dog('lucy', 3)
your_dog.sit()
your_dog.roll_over()


# restaurant
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):  # the parameter are only
        # used in init function
        self.name = restaurant_name  # self.nameofnewvariable (instance variable)=parameter of init function
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print("The name of the restaurant is " + self.name.title())
        print("It is a " + self.cuisine.title() + " type restaurant.")

    def open_restaurant(self):
        print("The restaurant " + self.name.title() + " is now open!")


my_restaurant = Restaurant('lilac', 'Asian fusion')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

# Three restaurants

your_restaurant = Restaurant('hotwind', 'italian')
your_restaurant.describe_restaurant()
your_restaurant.open_restaurant()


# Users

class User():
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name

    def info(self, username, password):
        self.username = username
        self.password = password

    def describe_user(self):
        print("This user " + self.firstname.title() + " "
              + self.lastname.title() + " has username: " + self.username
              + " and password: " + str(self.password))

    def greet_user(self):
        print("Welcome " + self.username + "!")


user1 = User('hanwei', 'li')
user1.info('lihanwei', 123456)
user1.greet_user()
user1.describe_user()


# working with classes and instances
# setting a default value for an attribute

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model  # self.nameofnewvariable (instance variable)=parameter/attribute of init function
        self.year = year
        self.odometer_reading = 0  # you can also put this line in the function paramter
        # you can decide whether to put odometer in parameter

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    # modifying an attribute's value through a method
    # some additional work to prevent anyone roll back the odometer reading
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


# modifying an attribute's value directly
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# simplest way is to access the attribute directly through an instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# modifying an attribute's value through a method
my_new_car.update_odometer(24)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# Number served
class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):  # the parameter are only
        # used in init function
        self.name = restaurant_name  # self.nameofnewvariable (instance variable)=parameter/attribute of init function
        # self.name create a variable of restaurant_name parameter.
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


my_restaurant = Restaurant('lilac', 'Asian fusion')
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
my_restaurant.number_served
my_restaurant.set_number_served(12)
my_restaurant.number_serve_read()

my_restaurant.number_served = 13
my_restaurant.number_serve_read()

my_restaurant.increment_number_served(23)
my_restaurant.number_serve_read()


# login attempts
# add an attribute called login_attempts to your user class

# Users

class User():
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.login_attempts = 0

    def info(self, username, password):
        self.username = username
        self.password = password

    def describe_user(self):
        print("This user " + self.firstname.title() + " "
              + self.lastname.title() + " has username: " + self.username
              + " and password: " + str(self.password))

    def greet_user(self):
        print("Welcome " + self.username + "!")

    def login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    def increment_login_attempts(self, increment_login):
        self.login_attempts += increment_login

    def reset_login_attempts(self):
        self.login_attempts = 0

    def view_login_attempts(self):
        print('User has logged in for ' + str(self.login_attempts))
        # when you use an variable in a class, use self.xxx


user1 = User('hanwei', 'li')
user1.info('lihanwei', 123456)
user1.greet_user()
user1.describe_user()

user1.increment_login_attempts(2)
user1.view_login_attempts()
user1.increment_login_attempts(4)
user1.view_login_attempts()
user1.reset_login_attempts()
user1.view_login_attempts()


# Inheritance.
# if the class you are writing is a specialized version of another class you wrote,
# you can use inheritance
# The __init__() method for a child class

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # you can also put this line in the function paramter
        # you can decide whether to put odometer in parameter
        self.gas_tank = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gas_tank(self, gas_tank):
        self.fill_gas_tank += gas_tank

# Instances as attributes
# you might recognize that part of one class can be written as a separate class
# then we can use a battery instance as an attribute in ElectricCar class

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElectricCar(Car):  # we define the child class, the name of the parent class must
    # be included in parentheses in the definition of the child class
    def __init__(self, make, model, year,):  # initialize attributes of the parent class
        super().__init__(make, model, year)
        # super() function helps python make connections between the parent and child
        # parent class - superclass, child class - subclass
        self.battery = Battery() # tells python to create a new instance of battery
        # and store that instance in the attribute self.battery
        # any ElectricCar instance will now have a Battery instance created automatically

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    # Overriding methods from the parent class
    def fill_gas_tank(self): # does it need the self here?
        print("This car doesn't need a gas tank")




my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()  # you need to call like this instead of using
# my_tesla.describe() why????
my_tesla.battery.get_range()


# an attribute that belong to any car, should be added to the Car class instead of
# the ElectricCar class


# Excercise: Icecream stand
# Inherit from restaurant class


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

# Add an attribute called flavours that stores a list of Icecream flavors
# write a method that displays these flavors.
# create an instance of Icecreamstand, and call this method


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

# inherit class only inherit the functions like in line 350
# only if you use the super().init, it will initialize the attributes that
# follow the function.like in line 351

# self = refers to instance of the current class
# super() = refers to instance of the parent class

icecreamstand1 = IcecreamStand('Vaniletta','icecream')

icecreamstand1.flavors = ['vanilla', 'chocolate', 'black cherry']
icecreamstand1.display_flavors()
icecreamstand1.describe_restaurant()

# Admin is a special class of user class
# add an attribute, priviledeges, that stores a list of strings like çan add post',
# write a method called show_priviledges()


# Users

class User():
    def __init__(self, first_name, last_name):
        self.firstname = first_name
        self.lastname = last_name
        self.login_attempts = 0

    def info(self, username, password):
        self.username = username
        self.password = password

    def describe_user(self):
        print("This user " + self.firstname.title() + " "
              + self.lastname.title() + " has username: " + self.username
              + " and password: " + str(self.password))

    def greet_user(self):
        print("Welcome " + self.username + "!")

    def login_attempts(self, login_attempts):
        self.login_attempts = login_attempts

    def increment_login_attempts(self, increment_login):
        self.login_attempts += increment_login

    def reset_login_attempts(self):
        self.login_attempts = 0

    def view_login_attempts(self):
        print('User has logged in for ' + str(self.login_attempts))
        # when you use an variable in a class, use self.xxx

class Admin(User):
    def __init__(self,first_name,last_name):
        super().__init__(first_name,last_name)
        self.privileges = ['can add post','can delete post']

    def show_privileges(self):
        print("\n The admin " + self.firstname.title() + " " + self.lastname.title()
              + " has the following priveleges: ")
        for privilege in self.privileges:
            print ("- " + privilege)

admin1 = Admin('mauri','mustonen')
admin1.show_privileges()



# battery upgrade
# add a method to the battery class called upgrade_battery()
# this method should check the battery size and set the capacity to 85 if
# it isn't already. Make an electric car with a default battery size,
# call get_range() once, and then call get_range() a second  time after upgrading
# the battery. You should see an increase in the car's range.

class Battery():
    def __init__(self,battery_size):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 85:
            print("The battery is already upgraded.")
            pass
        else:
            self.battery_size == 85
            print("Upgraded the battery to 85 kWh.")


class ElectricCar(Car):  # we define the child class, the name of the parent class must
    # be included in parentheses in the definition of the child class
    def __init__(self, make, model, year,):  # initialize attributes of the parent class
        super().__init__(make, model, year)
        # super() function helps python make connections between the parent and child
        # parent class - superclass, child class - subclass
        self.battery = Battery(battery_size=70) # tells python to create a new instance of battery
        # and store that instance in the attribute self.battery
        # any ElectricCar instance will now have a Battery instance created automatically

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

    # Overriding methods from the parent class
    def fill_gas_tank(self): # does it need the self here?
        print("This car doesn't need a gas tank")

car1 = ElectricCar('honda','ranger','2020')
car1.battery.battery_size
car1.battery.get_range()
car1.battery.upgrade_battery()
car1.battery.get_range()


# when you inherit a class, you override function
# google for override



# Importing classes
# python lets you store classes in modules and then import the classes you need into
# your main program.
