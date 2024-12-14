class Bird:
    wings = True

    def __init__(self, color, specie):
        self.color = color
        self.specie = specie

    def tweet(self):
        print(f'Tweet! My color is {self.color}.')

    def fly(self, meters):
        print(f'The bird flew {meters} meters.')
        self.tweet()

    def change_color(self):
        self.color = 'Black'
        print(f'Now the bird it\'s {self.color}')

    @classmethod
    def lay_eggs(cls, cantity):
        print(f'Lay {cantity} eggs!')

    @staticmethod
    def watch():
        print('The bird watch...')


Bird.watch()