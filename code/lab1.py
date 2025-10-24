class Car:
    def __init__(self, make, model): # конструктор класса
        self.make = make # обращение к атрибуту класса
        self.model = model # обращение к атрибуту класса

my_car = Car('Toyota', 'Corolla') # вызываем конструктор класса, передаем параметры make и model
print(my_car.make, my_car.model)