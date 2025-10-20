with open('code/input.txt', 'a+') as f:
    f.write('\nТеперь тут 3 строки')

with open('code/input.txt', 'r') as f:
    lines = f.readlines()
    print(lines)