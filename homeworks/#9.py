def add(x, y):
    return x + y

def substract(x, y):
    return x - y


while True:
    print("1. Add\n"
          + "2. Subtract"
          )
    menu_calculator = int(input("Type your chose:"))
    if menu_calculator == 1:
        number_1 = int(input("Enter your first number: "))
        number_2 = int(input("Enter your second number: "))
        result = number_1 + number_2

        print(number_1,"+",number_2, "=", add(number_1, number_2))

        with open('file.txt', 'r') as file:
            print(file.read())

        with open('file.txt', 'a') as file:
            file.write(f'\n{number_1} + {number_2} = {result} '
                       )


    if menu_calculator == 2:
        number_1 = int(input("Enter your first number: "))
        number_2 = int(input("Enter your second number: "))
        result = number_1 - number_2

        print(number_1,"-",number_2, "=", substract(number_1, number_2))


        with open('file.txt', 'r') as file:
            print(file.read())

        with open('file.txt', 'a') as file:
            file.write(f'\n{number_1} - {number_2} = {result} '
                       )









if menu_calculator == 2:
    calculator_substract(number_1, number_2)
number_1 = int(input("Enter your first number: "))
number_2 = int(input("Enter your second number: "))
