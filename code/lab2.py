class Car:
    def __init__(self, make, model): # конструктор класса
        self.make = make # обращение к атрибуту класса
        self.model = model # обращение к атрибуту класса
    def drive(self): # создали метод
        print(f'Driving the {self.make} {self.model}')
my_car = Car('Toyota', 'Corolla') # вызываем конструктор класса, передаем параметры make и model
my_car.drive() # вызываем метод