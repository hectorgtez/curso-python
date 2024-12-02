precios_cafe = [('Capuchino', 1.5), ('Expresso', 2.5), ('Moka', 1.9)]

def cafe_mas_caro(lista_cafes):
    precio_mayor = 0
    nombre_cafe = ''

    for cafe, precio in lista_cafes:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe = cafe

    return nombre_cafe, precio_mayor

cafe, precio = cafe_mas_caro(precios_cafe)
print(f'El café más caro es {cafe} cuyo precio es {precio}')