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


# you called func(4, 4, 4)
# it returned 6