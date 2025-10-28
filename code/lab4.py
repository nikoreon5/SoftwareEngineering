class Mammal:
    className = 'Mammal'

class Dog(Mammal):
    species = 'canine'
    sounds = 'wow'
    def bite(self):
        print('You were bitten')

class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'
    def murr(self):
        print('Murrrrrrr...')

dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
dog.bite()
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
cat.murr()