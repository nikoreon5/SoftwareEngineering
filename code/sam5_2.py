from math import sqrt
def calcTriangleSquare(a, b, c):
    p = (a + b  + c) / 2
    result = sqrt(p * (p - a) * (p -b) * (p - c))
    return result