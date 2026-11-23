def base_decorator(function):
    def wrapper():
        # before calculation
        result = function()
        # after calculation
        return result
    return wrapper



def round_number(function):

    def wrapper(*args):
        print('args', args)
        print('args one by one', *args)

        # before calculation
        print(function)
        result = function(*args)
        # after calculation

        result = round(result, 2)
        return result

    return wrapper




@round_number
def get_pi() -> float:
    return 3.14159265359


@round_number
def multiply_number_to_3(number: float) -> float:
    result = number * 3
    # result = round(result, 5)
    return result

@round_number
def multiply_numbers(number1: float, number2: float) -> float:
    result = number1 * number2
    # result = round(result, 5)
    return result

@round_number
def divide_number_to_3(number: float) -> float:
    result = number / 3
    # result = round(result, 5)
    return result



# print(get_pi)

pi = get_pi()
print(pi)

r3 = multiply_number_to_3(3.12333333333331465,)
print(r3)


r = divide_number_to_3(2.6)
print(r)

r = divide_number_to_3(2.653543)
print(r)
r = divide_number_to_3(2.63231)
print(r)
r = divide_number_to_3(212312.6)
print(r)
r = divide_number_to_3(23213123.6321313)
print(r)


r2 = multiply_numbers(2.3541, 3.987874545)
print(r2)




