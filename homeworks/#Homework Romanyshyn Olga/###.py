# 1. Write the method that returns the number of threads currently in execution.
# Also, prepare the method that will be executed with threads and run during the first method counting.
# (multithreading)
#
# 2. Write a program that will calculate two quadratic equations (6x² + 11x - 35 = 0. and 5x² - 2x - 9 = 0.)
# at the same time, set all the parameters of the equation in variables. (mult

from multiprocessing import Process
import os



print('Решаем уравнение a•x²+b•x-c=0')
a = input('Введите значение a: ')
b = input('Введите значение b: ')
c = input('Введите значение c: ')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('Дискриминант = ' + str(discriminant))
if discriminant < 0:
    print('Корней нет')
elif discriminant == 0:
    x = -b / (2 * a)
    print('x = ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))