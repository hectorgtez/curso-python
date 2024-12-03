def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')

    for arg in args:
        print(f'arg = {arg}')

    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')

args_prueba = [100, 200, 300, 400]
kwargs_prueba = {'x':'uno', 'y':'dos', 'z':'tres'}
prueba(15, 50, *args_prueba, **kwargs_prueba)