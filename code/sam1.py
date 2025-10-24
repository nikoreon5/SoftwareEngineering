class Switch:
    def __init__(self, model, portsCount, poe):
        self.model = model
        self.portsCount = portsCount
        self.poe = poe

mySwitch = Switch('Eltex MES2348P', 48, True)
print(mySwitch.model, mySwitch.portsCount, mySwitch.poe)