def check_logger(func_1):
    def type_logger(func):
        def wrapper(x):
            if not func_1(x):
                raise ValueError(f'Wrong value {x}')

            print(func(x))

        return wrapper

    return type_logger


@check_logger(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(10)
