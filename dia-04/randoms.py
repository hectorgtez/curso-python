from random import *

colores = ['Morado', 'Azul', 'Blanco']

# aleatorio = randint(1, 50)
# aleatorio = round( uniform(1, 5), 1 )
# aleatorio = random()
aleatorio = choice(colores)

print(aleatorio)

numeros = list( range(5, 51, 5) )
shuffle(numeros)

print(numeros)