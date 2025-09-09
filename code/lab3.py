numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input('Введите число: '))
if n in numbers:
    print(f'Число {n} есть в массиве {numbers}')
else:
    print(f'Числа {n} нет в массиве {numbers}')