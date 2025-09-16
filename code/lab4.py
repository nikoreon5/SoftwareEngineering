def main(*args):
    sum = 0
    for i in range(len(args) - 1):
        print(f'Прибавляем к сумме = {sum} {args[i]} * {args[i + 1]}, получаем {sum + args[i] * args[i + 1]}')
        sum += args[i] * args[i + 1]
    return sum
main(1, 2, 3, 4, 5, 6)