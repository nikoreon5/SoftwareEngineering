from sam5_2 import calcTriangleSquare
def main():
    a, b, c = map(int, input('Введите три стороны треугольника через пробел: ').split())
    result = calcTriangleSquare(a, b, c)
    print(f'Результат: {result}')
main()