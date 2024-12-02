def checar_3_cifras(lista):
    lista_cumplen = []
    for n in lista:
        if n in range(100, 1000):
           lista_cumplen.append(n)
        else:
            pass

    return lista_cumplen

resultado = checar_3_cifras([1, 2, 3, 1000, 200])
print(resultado)