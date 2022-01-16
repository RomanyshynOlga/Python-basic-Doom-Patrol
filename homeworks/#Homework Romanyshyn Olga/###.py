def logged(func):
    def inner(*args):
        result = func(*args)
        return result

    return inner


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))