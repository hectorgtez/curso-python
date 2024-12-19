class Cow:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} says moo!')

class Sheep:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'{self.name} says mee!')

cow1 = Cow('Aurora')
sheep1 = Sheep('Cloud')

animals = [cow1, sheep1]

def animal_talk(animal):
    animal.talk()

animal_talk(sheep1)