from functools import wraps
from datetime import datetime

ADMIN= {
    'login': 'a',
    'password': '1'
}

def admin_decorator(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        print(111111111111111111111111111)
        # before calculation
        password = input('Enter password')
        login = input('Enter login')
        if login == ADMIN['login'] and password == ADMIN['password']:
            result = function(*args, **kwargs)
            # after calculation
            print(4444444444444444444444444444444444)
            return result
        print("NOT ALLOWED")
        return None

    return wrapper


def log_decorator(log_file: str = 'log.csv'):
    def wrapper_1(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            print(2222222222222222222222222222222)
            # before calculation
            result = function(*args, **kwargs)
            # after calculation
            with open(log_file, mode='a', encoding='utf-8') as file:
                file.write(f"{datetime.now()};{function.__name__};{args};{kwargs};{result}\n")

            print(333333333333333333333333333333333333)
            return result

        return wrapper
    return wrapper_1


@log_decorator('log_pi.csv')
def get_pi() -> float:
    """
    some info about PI
    """
    return 3.14159265359


@admin_decorator
@log_decorator()
def divide_numbers(number1: float, number2: float) -> float:
    result = number1 / number2
    return result

@admin_decorator
@log_decorator()
def multiply_number_to_3(number: float) -> float:
    result = number * 3
    return result

divide_numbers(2, 9)
multiply_number_to_3(9)
get_pi()
