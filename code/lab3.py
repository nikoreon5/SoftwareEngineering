from lab2 import Car
class ElectricCar(Car): # наследуемся от Car
    def __init__(self, make, model, batteryCapacity):
        super().__init__(make, model) # вызываем конструктор класса Car
        self.batteryCapacity = batteryCapacity # добавляем еще одно поле
    def charge(self): # добавляем еще один метод
        print(f'Charging the {self.make} {self.model} with {self.batteryCapacity} kWh')

myElectricCar = ElectricCar('Tesla', 'Model S', 75) # вызываем конструктор
myElectricCar.drive()
myElectricCar.charge()