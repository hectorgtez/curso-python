class Bird:
    wings = True

    def __init__(self, color, specie):
        self.color = color
        self.specie = specie

bird = Bird('Red', 'Tucan')
print(f'My bird is a {bird.specie}, and it\'s color is {bird.color}')
print(bird.wings)
print(Bird.wings)