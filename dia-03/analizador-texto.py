sentence = input('Ingresa una frase: ').lower()
letters = list( input('Ingresa 3 letras: ').lower() )

splited_sentence = sentence.split()

# Cantidad de veces que aparecen cada letra
print(f'\nVeces que aparece la letra "{ letters[0].upper() }": { sentence.count(letters[0]) }')
print(f'Veces que aparece la letra "{ letters[1].upper() }": { sentence.count(letters[1]) }')
print(f'Veces que aparece la letra "{ letters[2].upper() }": { sentence.count(letters[2]) }')

# Palabras totales en la frase
print(f'\nCantidad de palabras en la frase: { len(splited_sentence) }')

# Primera y ultima letra de la frase
print(f'\nPrimer letra de la frase: "{ sentence[0].upper() }"')
print(f'Última letra de la frase: "{ sentence[-1].upper() }"')

# Orden inverso de las palabras
splited_sentence.reverse()
print(f'\nPalabras de la frase en orden inverso:\n{ ' '.join(splited_sentence) }')

# Aparece python en la frase
dic = {True:'Si', False:'No'}
print( f'\n{ dic['python' in sentence] } contiene la palabra "Python"' )