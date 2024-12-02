from random import shuffle

def mezclar(lista):
    shuffle(lista)

    return lista

def probar_suerte():
    intento = ''
    while intento not in ['1', '2', '3', '4']:
        intento = input('Elige un número del 1 al 4: ')

    return int(intento)

def checar_intento(lista, intento):
    if lista[intento - 1] == '-':
        print('\nA lavar los platos!')
    else:
        print('\nTe has salvado esta vez...')

    print(f'Te ha tocado {lista[intento - 1]}')

palitos = mezclar(['-', '--', '---', '----'])
seleccion = probar_suerte()
checar_intento(palitos, seleccion)
