from sam2 import Switch

class ManageableSwitch(Switch):
    def __init__(self, model, portsCount, poe, ip):
        super().__init__(model, portsCount, poe)
        self.__ip = ip
    def getInfo(self):
        return f"Коммутатор {self.model}, IP: {self.__ip}"

class Router(Switch):
    def __init__(self, model, portsCount, poe, ip):
        super().__init__(model, portsCount, poe)
        self.__ip = ip
    def getInfo(self):
        return f"Маршрутизатор {self.model}, IP: {self.__ip}"

def show_device_info(device):
    print(device.getInfo())

switch = ManageableSwitch("Eltex MES234B", 48, False, "10.10.10.109")
router = Router("Cisco 2901", 4, False, "192.168.1.1")

show_device_info(switch)
show_device_info(router)