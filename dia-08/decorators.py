def decorate_greeting(function):
    def other_func(text):
        print('Hi!')
        function(text)
        print('Goodbye...')
    return other_func


def uppercase(text):
    print(text.upper())


def lowercase(text):
    print(text.lower())


upper_decorated = decorate_greeting(uppercase)
upper_decorated('python')