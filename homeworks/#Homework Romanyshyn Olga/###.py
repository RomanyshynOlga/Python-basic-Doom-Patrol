# 1. Write the method that returns the number of threads currently in execution.
# Also, prepare the method that will be executed with threads and run during the first method counting.
# (multithreading)
#
# 2. Write a program that will calculate two quadratic equations (6x² + 11x - 35 = 0. and 5x² - 2x - 9 = 0.)
# at the same time, set all the parameters of the equation in variables. (mult








#2
import threading

print('Calculate quadratic equations  a•x²+b•x-c=0')


def foo(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print('There are no roots')
    elif discriminant == 0:
        x = -b / (2 * a)
        print('x = ' + str(x))
    else:
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        print('x₁ = ' + str(x1))
        print('x₂ = ' + str(x2))


equations1 = threading.Thread(target=foo(6, 11, -35))
equations2 = threading.Thread(target=foo(5, -2, -9))

equations1.start()
equations2.start()


