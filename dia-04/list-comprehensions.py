lista = [letra for letra in 'python']
print(lista)

pies = [10, 20, 30, 40, 50]
metros = [round( p / 3.281, 2) for p in pies]
print(metros)

lista = [n for n in range(0, 21, 2) if (n * 2 > 10)]
lista2 = [n if (n * 2 > 10) else 'NO' for n in range(0, 21, 2) ]
print(lista2)