#1

def add(a, b):
    return a + b


add(5, 5)  # 10

def double_result(num):
    def inner(method):
        def multiply_method(a, b):
            return method(a, b) * num
        return multiply_method
    return inner


@double_result(2)
def add(a, b):
    return a + b


print(add(5, 5))
#20



#2
def only_odd_parameters(func):
    def inner(*args):
        for i in args:
            if i % 2 != 0:
                return func(*args)
            else:
                return "Please use only odd numbers!"

    return inner

@only_odd_parameters
def add(a, b):
    return a + b


print(add(5, 5))  # 10
print(add(4, 4))  # "Please use only odd numbers!"


@only_odd_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e
print (multiply(5, 5, 5, 5, 5))
print (multiply(1, 2, 3, 4, 5))



#3

def logged(func):
    def inner(*args):
        result = func(*args)
        return result
    return inner
    # log function arguments and its return value



@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))








#4
def type_check(correct_type):
    def inner(foo):
        def another_function(arg):
            if(isinstance(arg, correct_type)):
                return foo(arg)
            else:
                return f"Wrong Type: {type(arg)}"
        return another_function
    return inner


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))  # "Wrong Type: string" should be printed, since non-int passed to decorated function


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))  # "Wrong Type: list" should be printed, since non-str passed to decorated function



