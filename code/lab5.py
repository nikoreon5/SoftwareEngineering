import math
class Shape: # базовый класс
    def area(self):
        pass
class Rectangle(Shape): # класс прямоугольника
    def __init__(self, width, height): # конструктор принимает ширину и высоту
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height # вычисляем площадь
class Circle(Shape): # класс круга
    def __init__(self, radius): # конструктор принимает радиус
        self.radius = radius
    def area(self):
        return math.pi * math.pow(self.radius, 2) # вычислям площадь

myRect = Rectangle(10, 10) # создаем объект класса прямоугольник
myCircle = Circle(7) # создаем объект класса круг
print(myRect.area()) # выводим на экран площадь прямоугольника
print(myCircle.area()) # выводим на экран площадь круга