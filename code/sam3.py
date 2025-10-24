from sam2 import Switch
class ManageableSwitch(Switch):
    def __init__(self, model, portsCount, poe, ip, ports):
        super().__init__(model, portsCount, poe)
        self.ip = ip
        self.ports = ports
    def configurePort(self, portNumber, config):
        self.ports[portNumber] = config
        print(f'Порт № {portNumber} настроен как {config}')

myManageableSwitch = ManageableSwitch('Eltex MES234B', 48, False, '10.10.10.109', [''])
myManageableSwitch.printInfo()
myManageableSwitch.configurePort(0, 'switchport mode access switchport access vlan 650')