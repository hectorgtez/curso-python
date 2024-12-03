def letras_unicas(palabra):
    lista_palabra = list( palabra.lower() )
    lista_unica = []

    for letra in lista_palabra:
        if letra not in lista_unica:
            lista_unica.append(letra)

    lista_unica.sort()
    return lista_unica

print( letras_unicas('entretenido') )