# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    car_type = 'my car'

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_max_speed(self):
        print(f'Max speed is {self.max_speed}')

    def print_mileage(self):
        print(f'All mileage is {self.mileage}')


my_car = Vehicle(250, 25)
my_car.print_mileage()
my_car.print_max_speed()


class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def print_bus(self):
        print(f'My bus have{self.seating_capacity} seating')


my_car = Bus(250, 150, 25)
my_car.print_bus()

# All mileage is25
# Max speed is 250
# My bus have25 seating


# 3. Determine which class a given Bus object belongs to (Check type of an object)
print(type(my_car))
# <class '__main__.Bus'>


# 4. Determine if School_bus is also an instance of the Vehicle class

school_bus = Bus(100, 50, 5)
print(isinstance(school_bus, Vehicle))


# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:

    def __init__(self, get_school_id, number_of_stude):
        self.get_school_id = get_school_id
        self.number_of_stude = number_of_stude


# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(Bus, School):

    def __init__(self, max_speed, mileage, seating_capacity, get_school_id, number_of_stude, bus_school_color):
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        School.__init__(self, get_school_id, number_of_stude)
        self.bus_school_color = bus_school_color

    def bus_school_color(self):
        print(f'It is {self.bus_school_color}')


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,



class Bear:
    type_Bear = "Polar_bear"

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'Bear can {self.sound}')


class Wolf:
    type_Wolf = "Dog"

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(f'Wolf can {self.sound}')


Polar_bear = Bear('growls')
Dog = Wolf('howls')
animals = (Polar_bear, Dog)

for animal_sound in animals:
    animal_sound.make_sound()
