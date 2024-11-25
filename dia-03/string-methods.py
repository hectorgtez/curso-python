# upper() - Mayusculas
# lower() - Minusculas
# split('caracter') - Dividir string por caracter (espacio es predeterminado)

text = 'Este es el texto de ejemplo'
result = text.upper()
print(result)

result = text.lower()
print(result)

result = text.split()
print(result)

a = 'Aprender'
b = 'Python'
c = 'es'
d = 'genial'
e = '-'.join([a, b, c, d])
print(e)

result = text.find('texto')
print(result)

result = text.replace('ejemplo', 'muestra')
print(result)