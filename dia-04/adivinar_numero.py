from random import randint

intentos_totales = 8
intentos_disponibles = intentos_totales
numero_secreto = randint(1, 100)
estimado = 0

nombre = input('¡Hola! ¿Cuál es tu nombre?: ')

print(f'Encantado {nombre}. Ya tengo el número listo para ser adivinado.')
print('El número secreto está en el rango de 1 al 100.')
print('Recuerda que tienes 8 intentos para tratar de encontrarlo.')

while intentos_disponibles > 0:
    print(f'\nTe quedan {intentos_disponibles} intentos...')
    estimado = int( input('¿Cuál es el número secreto?: ') )
    intentos_disponibles -= 1

    if estimado not in range(1, 101):
        print('\nOye, recuerda que el número está entre 1 y 100...\nIngresa un valor válio por favor.')
        continue
    elif estimado < numero_secreto:
        print('\n¡Uy! Has fallado. El número secreto es mayor.')
    elif estimado > numero_secreto:
        print('\n¡Uuff! Por poco. El número secreto es menor.')
    else:
        print(f'\n¡Felicidades {nombre}, has encontrado el número secreto!')
        print(f'Solo te tomó {intentos_totales - intentos_disponibles} intentos lograrlo.')
        break
else:
    if estimado != numero_secreto:
        print('\nLo siento, se agotaron los intentos.')
        print(f'El número secreto era {numero_secreto}.')
        print('Has perdido... ¡Suerte para la próxima!')