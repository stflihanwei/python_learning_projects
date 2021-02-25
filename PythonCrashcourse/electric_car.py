from car import Car
class ElectricCar(Car):  # we define the child class, the name of the parent class must
    # be included in parentheses in the definition of the child class
    def __init__(self, make, model, year,):
        super().__init__(make, model, year)  # initialize attributes of the parent class
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
