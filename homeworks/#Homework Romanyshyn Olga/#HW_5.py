#1.


class Laptop:
    def __init__(self):
        battery_1 = Battery('When not charging, use battery_1')
        battery_2 = Battery('When not charging, use battery_2')
        self.battery = (battery_1, battery_2)


class Battery:
    def __init__(self, charging):
        self.charging = charging


laptop = Laptop()
print(laptop.battery[0].charging)

# When not charging, use battery_1




#2


class Guitar:
    def __init__(self, yamaha):
        self.yamaha = yamaha

class GuitarString:
    def __init__(self):
        pass

yamaha = GuitarString()
guitar = Guitar(yamaha)


#3

class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c

print(Calc.add_nums(1, 2, 3))




#4

class Pasta:
    TYPES = ("carbonara", "bolognaise")

    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __str__(self):
        return (f'Pasta {self.ingredients}')


    @classmethod

    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])


    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

pasta_carbonara = Pasta.carbonara()
pasta_bolognaise = Pasta.bolognaise()
print(pasta_carbonara)
print(pasta_bolognaise)



#5 PASS


#6"""
   # Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
import dataclasses


@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


Anton_home = AddressBookDataClass(key=25, name='Anton', phone_number='2972048', address='Lviv', email='a@gmait.com', birthday='16/11/92', age=29)
print(Anton_home)



#7 Create the same class (6) but using NamedTuple

from collections import namedtuple

AddressBookDataClass = namedtuple('AddressBookDataClass',['key', 'name', 'phone_number', 'address', 'email', 'birthday', 'age'])
AddressBookDataClassNew = AddressBookDataClass(25, 'Anton', '2972048', 'Lviv', 'a@gmait.com', '16/11/92', 29)
print(AddressBookDataClassNew)

8#class AddressBook:


class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__ (self):
        return f'AddressBook{self.key}, {self.name},{self.phone_number}, {self.address}, {self.email}, {self.birthday}, {self.age}'

AddressBook_NEW = AddressBook( 25, 'Anton', '2972048', 'Lviv', 'a@gmait.com', '16/11/92', 29)


print(AddressBook_NEW)


#9
class Person:
    name = "John"
    age = 36
    country = "USA"

john = Person()
print(john.age)
#36
setattr(john,'age',20)
print(john.age)
#20
print(john.name, john.age, john.country)
#John 20 USA




#10
class Student:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def print_student(self):
        print(f'The student  with {self.id} name is {self.name} ')

student_1 = Student (22, 'Olga')
print(student_1)
setattr(student_1,'email', 'rob@dmail')
print(getattr(student_1, 'email'))

#11/

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature * 1.8 + 32


temperature_1 = Celsius(10)
print(temperature_1.temperature)