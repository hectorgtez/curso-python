lista = ['a', 'b', 'c']

for indice, item in enumerate(lista):
    print(f'{indice+1}. {item}')

tuples = list(enumerate(lista))
print(tuples)