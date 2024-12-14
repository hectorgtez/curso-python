class Bird:
    wings = True

    def __init__(self, color, specie):
        self.color = color
        self.specie = specie

    def tweet(self):
        print(f'Tweet! My color is {self.color}.')

    def fly(self, meters):
        print(f'The bird flew {meters} meters.')

bird = Bird('Yellow', 'Canary')
bird.tweet()
bird.fly(10)