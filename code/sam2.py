class Switch:
    def __init__(self, model, portsCount, poe):
        self.model = model
        self.portsCount = portsCount
        self.poe = poe
    def printInfo(self):
        print(f'----- Информация об оборудовании -----\nМодель: {self.model}\nКоличество портов: {self.portsCount}\nНаличие PoE: {self.poe}')
mySwitch = Switch('Eltex MES2348P', 48, True)
mySwitch.printInfo()