def removeFirstAppearance(my_tuple, num):
    result = []
    found = False
    for number in my_tuple:
        if number == num:
            if not(found):
                found = True
            else:
                result.append(number)
        if number != num:
            result.append(number)
    return tuple(result)
print(removeFirstAppearance((1, 2, 3), 1))
print(removeFirstAppearance((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(removeFirstAppearance((2, 4, 6, 6, 4, 2), 9))