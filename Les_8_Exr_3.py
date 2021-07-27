def type_logger(func):
    def wrapper(*args, ):
        _list = args
        print(_list)

        b = (f'{el}: {type(el)}' for el in _list)
        print(*b)

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(3, 4)
