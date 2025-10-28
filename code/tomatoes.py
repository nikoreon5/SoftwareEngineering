class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}
    def __init__(self, _index):
        self._index = _index # защищенный атрибут
        self._state = self.states[_index] # защищенный атрибут
    def grow(self):
        if not self.is_ripe():
            self._index += 1
            self._state = self.states[self._index]
    def is_ripe(self):
        return self._index == 3

class TomatoBush:
    def __init__(self, tomatoesCount):
        self.tomatoes = []
        for i in range(tomatoesCount):
            self.tomatoes.append(Tomato(0))
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()
    def are_all_ripe(self):
        for tomato in self.tomatoes:
            if not tomato.is_ripe():
                return False
        return True
    def give_away_all(self):
        self.tomatoes = []

class Gardener:
    def __init__(self, name, _plant):
        self.name = name # открытый атрибут
        self._plant = _plant # защищенный атрибут
    def work(self):
        self._plant.grow_all()
        print(f"{self.name} ухаживает за растением.")
    def harvest(self):
        if self._plant.are_all_ripe():
            print('Все помидоры сзрели. Урожай собран успешно.')
            self._plant.give_away_all()
        else:
            print('Невозможно собрать урожай: есть недозревшие плоды.')
    def knowledge_base(self):
        print('Справка: ухаживайте за растениями, чтобы они созревали. Когда плоды созреют, можно будет собрать урожай.')

tomatoBush = TomatoBush(5)
gardener = Gardener('Анатолий', tomatoBush)
gardener.work()
gardener.harvest()
gardener.work()
gardener.work() 
gardener.harvest()