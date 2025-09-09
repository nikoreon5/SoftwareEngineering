x = int(input('Введите значение переменной: '))
if x < 0:
    print(f'{x} < 0')
elif x > 0 and x < 10:
    print(f'0 < {x} < 10')
else:
    print(f'{x} > 10')