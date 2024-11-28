lista = ['Pablo', 'Laura', 'Fede', 'Luis', 'Julia']

for nombre in lista:
    if nombre.startswith('L'):
        print(nombre)
    else:
        print('Este nombre no inicia con L')

numeros = [1, 2, 3, 4, 5]
value = 0

for numero in numeros:
    value = value + numero

print(value)