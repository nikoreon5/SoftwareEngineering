numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input('Введите число: '))
if n in numbers:
    if n % 2 == 0:
        print(f'Число {n} - четное и оно есть в массиве {numbers}')
    else:
        print(f'Числа {n} - нечетное и оно есть в массиве {numbers}')
else:
    print(f'Числа {n} нет в массиве {numbers}')