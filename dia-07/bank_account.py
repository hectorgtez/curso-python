from random import randint
from os import system

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

class Client(Person):
    def __init__(self, first_name, last_name, account_number, balance = 0):
        super().__init__(first_name, last_name)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}\nAccount Number: {self.account_number}\nBalance: ${self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print('\nAmount succesfully deposited!')

    def withdraw(self, amount):
        self.balance -= amount
        print('\nAmount succesfully withdrawn!')

def wait_and_clean_console():
    input('Press a key to continue...')
    system('cls')

def create_client():
    print('Hi! Welcome to Guzy Bank.')
    print('Let\'s create your new account.')

    f_name = input('\nEnter your first name: ')
    l_name = input('Enter your last name: ')
    acc_number = randint(100000, 999999)

    print(f'\nThanks {f_name} {l_name}, your account has been created successfully.')
    print(f'Your account number is {acc_number}, and your balance is $0.')

    return Client(f_name, l_name, acc_number)

def start_deposit(client):
    amount = -1
    print()
    while amount < 1:
        amount = int( input('Enter the amount: ') )
        if amount < 1:
            print('Invalid amount...')
            wait_and_clean_console()

    client.deposit(amount)
    wait_and_clean_console()

def start_withdraw(client):
    amount = -1
    print()
    while amount not in range(1, client.balance+1):
        amount = int( input('Enter the amount: ') )
        if amount not in range(1, client.balance+1):
            print('Invalid amount...')
            wait_and_clean_console()

    client.withdraw(amount)
    wait_and_clean_console()

def start(client):
    option = -1
    while option != 3:
        print(client)
        print('[1] Deposit')
        print('[2] Withdraw')
        print('[3] Exit')
        option = int( input('Select an option: ') )

        match option:
            case 1:
                start_deposit(client)
            case 2:
                start_withdraw(client)
            case 3:
                print('\nThanks for your visit!')
                break
            case _:
                print('\nInvalid input...')
                wait_and_clean_console()

new_client = create_client()
wait_and_clean_console()
start(new_client)