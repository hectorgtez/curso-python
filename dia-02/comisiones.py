nombre = input('¿Cuál es tu nombre?: ')
ventas = input('¿Cuáles fueron tus ventas totales del mes?: ')

ventas = float(ventas)
comision = ventas * 0.13
comision = round(comision, 2)

print(f'\nHola, {nombre}!')
print(f'Tus ventas fueron de ${ventas}')
print(f'Por lo tanto, tu comisión es de ${comision}')