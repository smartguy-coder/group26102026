some_sequence = 1111, 2222222, 333333, 444444, 55555555, 66666666
# print(some_sequence)

# print(id(some_sequence))
# print(id(some_sequence[0]))
# print(id(some_sequence[1]))
# print(id(some_sequence[2]))


# first = some_sequence[0]
# second = some_sequence[1]
# third = some_sequence[2]

first, second, third, *rest = some_sequence


# print(second)
print(rest)
print([444444, 55555555, 66666666])
print(*rest)
print(444444, 55555555, 66666666)

