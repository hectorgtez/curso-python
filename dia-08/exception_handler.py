def ask_number():
    while True:
        try:
            number = int( input('Enter a number: ') )
        except:
            print('That\'s not a number')
        else:
            print(f'Your input is {number}')
            break
    print('Thanks!')

ask_number()