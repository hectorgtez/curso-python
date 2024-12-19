class Father:
    def speak(self):
        print('Hi!')

class Mother:
    def laugh(self):
        print('Ja Ja!')

    def speak(self):
        print('How are you?')

class Son(Father, Mother):
    pass

class Grandson(Son):
    pass

grandson = Grandson()
grandson.speak()