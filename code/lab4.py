class Car:
    def __init__(self, make, model): # конструктор класса
        self._make = make # защищенный атрибут
        self.__model = model # приватный атрибут
    def drive(self): # создали метод
        print(f'Driving the {self._make} {self.__model}')
my_car = Car('Toyota', 'Corolla') # вызываем конструктор класса, передаем параметры make и model
my_car.drive()
print(my_car._make)
print(my_car.__model) # будет ошибка