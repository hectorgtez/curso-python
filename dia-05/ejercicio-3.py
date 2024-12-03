def contar_ceros(*args):
    contador = 0

    for n in args:
        if n == 0:
            contador += 1
            if contador >= 2:
                return True
        else:
            contador = 0

    return False

print( contar_ceros(1, 2, 0, 4, 0, 0, 7) )