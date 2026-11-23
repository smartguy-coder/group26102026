# n = 5
# print(id(n))


# print
# print(       id(print        )                        )
#
# something = print
# print(       id(something        )                        )
#
# something(9999999999999)
#
# print(       print               )
# print(       something               )


def some_new_function():
    print('function some_new_function was called - let`s dance')

def some_new_function_jump():
    print('function some_new_function_jump was called - let`s jumping')

# some_new_function()

# some_new_function
# print(some_new_function                )


def func_with_param(function):
    print('function func_with_param was called')

    def wrapper():
        print('function wrapper was called')
        print(id(function))
        print(function             )

        print("before")
        function()  # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print("after")

        print('take a rest')
        print('take a photo')
        return 5555

    return wrapper


# data = 56565656
# print(id(data))
# func_with_param(data)
# func_with_param(66666666666666)
# func_with_param(some_new_function)

some_new_function = func_with_param(                   some_new_function                         )
some_new_function_jump = func_with_param(some_new_function_jump)

print(some_new_function)

money1 = some_new_function()
print(money1)
print("--------------------------")
money2 = some_new_function()
print(money2)
print("--------------------------")
money3 = some_new_function_jump()
print(money3)
print("--------------------------")
