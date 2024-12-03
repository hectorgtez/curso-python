from random import choice

def mostrar_guiones(lista_guiones):
    print( ' '.join(lista_guiones) )

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Letra: ').lower()

        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('Entrada inválida...\n')

    return letra_elegida

def validar_letra(letra):
    if letra in lista_incorrectas:
        return False
    elif letra in palabra_secreta:
        return True
    else:
        lista_incorrectas.append(letra)
        return False

def sustituir_guiones(ingreso):
    index = 0
    for letra in palabra_secreta:
        if letra == ingreso:
            guiones[index] = ingreso
        index += 1

    return guiones

def validar_ganar(lista_guiones):
    if palabra_secreta == ''.join(lista_guiones):
        return True
    else:
        return False

lista_palabras = ['ballena', 'perro', 'murcielago']
palabra_secreta = choice(lista_palabras)
lista_incorrectas = []
guiones = []
vidas = 3

for i in palabra_secreta:
    guiones.append('_')

while vidas > 0:
    mostrar_guiones(guiones)
    eleccion = pedir_letra()

    if validar_letra(eleccion):
        guiones = sustituir_guiones(eleccion)

        if validar_ganar(guiones):
            print('\n¡Has ganado!')
            print(f'La palabra secreta era {palabra_secreta}.')
            break

        print()
    else:
        vidas -= 1
        print(f'{eleccion} no está en la palabra...')
        print(f'Letras incorrectas: {lista_incorrectas}')
        print(f'Te quedan {vidas} vidas.\n')
else:
    print('Has perdido...')
    print(f'La palabra secreta era {palabra_secreta}.')