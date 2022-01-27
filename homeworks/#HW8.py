def create_file():
    file = open('file.txt', 'w')
    file.write(file.txt)
    file.close()
    return open('file.txt', 'w')


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
            file = open('file.txt', 'r')
        except FileNotFoundError:
            file = create_file()

        with open('file.txt', 'r') as file:
            print()

        with open('file.txt', 'a') as file:
            file.write(f'\n {number_1} + {number_2} = {result} ')

    if menu_calculator == 2:
        number_1 = int(input("Enter your first number: "))
        number_2 = int(input("Enter your second number: "))
        result = number_1 - number_2

        print(number_1, "-", number_2, "=", substract(number_1, number_2))

        try:
            file = open('file.txt', 'r')
        except FileNotFoundError:
            file = create_file()

        with open('file.txt', 'r') as file:
            print()

        with open('file.txt', 'a') as file:
            file.write(f'\n {number_1} - {number_2} = {result} ')
