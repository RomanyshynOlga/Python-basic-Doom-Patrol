import logging
import os


def create_file():
    if os.path.exists('database') == False:
        os.mkdir('database')
    file = open('fileTT.txt', 'w')
    file.write('fileTT.txt')
    file.close()
    return open('fileTT.txt', 'r')


def add(x, y):
    return x + y


def substract(x, y):
    return x - y


while True:
    print("1. Add  " + "2. Subtract")
    menu_calculator = int(input("Type your chose:"))
    if menu_calculator == 1:
        number_1 = int(input("Enter your first number: "))
        number_2 = int(input("Enter your second number: "))
        result = number_1 + number_2

        print(number_1, "+", number_2, "=", add(number_1, number_2))

        try:
            file = open('fileTT.txt', 'r')
        except FileNotFoundError:
            logging.critical('File Not Found Error! Automatically Create file')
            file = create_file()

        with open('fileTT.txt', 'r') as file:
            print()

        with open('fileTT.txt', 'a') as file:
            file.write(f'\n {number_1} + {number_2} = {result} ')

    if menu_calculator == 2:
        number_1 = int(input("Enter your first number: "))
        number_2 = int(input("Enter your second number: "))
        result = number_1 - number_2

        print(number_1, "-", number_2, "=", substract(number_1, number_2))

        try:
            file = open('fileTT.txt', 'r')
        except FileNotFoundError:
            logging.critical('File Not Found Error! Automatically Create file')
            file = create_file()

        with open('fileTT.txt', 'r') as file:
            print()

        with open('fileTT.txt', 'a') as file:
            file.write(f'\n {number_1} - {number_2} = {result} ')
