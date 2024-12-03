def devolver_distintos(num1, num2, num3):
    lista = [num1, num2, num3]
    lista.sort()

    suma = num1 + num2 + num3

    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        return lista[1]

print( devolver_distintos(3, 5, 2) )