from random import randint
def cubeGame():
    n = randint(1, 6)
    print(f'На кубике выпало {n}')
    if n == 3 or n == 4:
        cubeGame()
    elif n == 5 or n == 6:
        print('Вы победили')
    elif n == 1 or n == 2:
        print('Вы проиграли')
if __name__ == '__main__':
    cubeGame()