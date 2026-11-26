from functools import wraps

def base_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        # before calculation
        result = function(*args, **kwargs)
        # after calculation
        return result
    return wrapper


def base_decorator_with_param(param: int = 2):
    def wrapper_1(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            # before calculation
            result = function(*args, **kwargs)
            # after calculation
            return result

        return wrapper
    return wrapper_1



def round_number(precision: int = 2):
    def wrapper_1(function):

        @wraps(function)
        def wrapper(*args, **kwargs):
            """
            this is a wrapper
            """
            print('args', args)
            print('args one by one', *args)
            print(kwargs)

            # before calculation
            print(function)
            result = function(*args, **kwargs)
            # after calculation

            result = round(result, precision)
            return result

        return wrapper
    return wrapper_1


@round_number(precision=3)
def get_pi() -> float:
    """
    some info about PI
    """
    return 3.14159265359


print(get_pi)
print(get_pi.__name__)
print(get_pi.__doc__)
# get_pi.number = 65
# print(get_pi.number)
# print(get_pi.__dict__)
# get_pi.__doc__ = 'dgdgjhdfjghdfjghjdfg'
# print(get_pi.__doc__)

@round_number(precision=4)
def multiply_number_to_3(number: float) -> float:
    result = number * 3
    # result = round(result, 5)
    return result

@round_number()
def multiply_numbers(number1: float, number2: float) -> float:
    result = number1 * number2
    # result = round(result, 5)
    return result

@round_number()
def divide_number_to_3(number: float) -> float:
    result = number / 3
    # result = round(result, 5)
    return result

@round_number(precision=5)
def divide_numbers(number1: float, number2: float) -> float:
    result = number1 / number2
    # result = round(result, 5)
    return result



# print(get_pi)

# pi = get_pi()
# print(pi)
#
# r3 = multiply_number_to_3(3.12333333333331465,)
# print(r3)
#
#
# r = divide_number_to_3(2.6)
# print(r)
#
# r = divide_number_to_3(2.653543)
# print(r)
# r = divide_number_to_3(2.63231)
# print(r)
# r = divide_number_to_3(212312.6)
# print(r)
# r = divide_number_to_3(23213123.6321313)
# print(r)
#
#
# r2 = multiply_numbers(2.3541, 3.987874545)
# print(r2)

# r2 = divide_numbers(10, number2=3)
# print(r2)
#
# get_pi()


