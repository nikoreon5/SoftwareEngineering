from sam2 import Switch
class ManageableSwitch(Switch):
    def __init__(self, model, portsCount, poe, ip, ports):
        super().__init__(model, portsCount, poe)
        self.__ip = ip
        self.__ports = ports
    def configurePort(self, portNumber, config):
        self.__ports[portNumber] = config
        print(f'Порт № {portNumber} настроен как {config}')
    def setIP(self, newIP):
        self.__ip = newIP
        print(f'IP-адрес изменен на {newIP}')
    def getIP(self):
        return self.__ip

myManageableSwitch = ManageableSwitch('Eltex MES234B', 48, False, '10.10.10.109', [''])
myManageableSwitch.printInfo()
print(f'Текущий IP-адрес: {myManageableSwitch.getIP()}')
myManageableSwitch.setIP('10.10.10.2')