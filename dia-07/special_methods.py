class CD:
    def __init__(self, author, title, tracks):
        self.author = author
        self.title = title
        self.tracks = tracks

    def __str__(self):
        return f'Album: {self.title} by {self.author}'

    def __len__(self):
        return self.tracks

    def __del__(self):
        print('CD has been eliminated.')

my_cd = CD('Pink Floyd', 'The Wall', 24)
print(my_cd)
print( len(my_cd) )
del my_cd