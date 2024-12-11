import os
from pathlib import Path
from os import system

base_path = Path.home() / 'Recetas'

def list_from_dir(path):
    return [folder.name for folder in path.iterdir()]

def print_list(items_list):
    idx = 1
    print()
    for item in items_list:
        print(f'{idx}. {item}')
        idx += 1

def read_recipe():
    # Get and print categories list
    categories = list_from_dir(base_path)
    print_list(categories)

    # Select category
    ctgr_selected = -1
    while ctgr_selected not in range(1, len(categories)+1):
        ctgr_selected = int( input('Elige la categoría: ') )

    # Get and print recipes list
    recipes = list_from_dir( Path(base_path / categories[ctgr_selected-1]) )
    print_list(recipes)

    # Select recipe
    rcp_selected = -1
    while rcp_selected not in range(1, len(recipes)+1):
        rcp_selected = int( input('Elige una receta: ') )

    # Read file and print content
    file_path = Path(base_path / categories[ctgr_selected-1] / recipes[rcp_selected-1])
    recipe_file = open(file_path)
    print(f'\n{ recipe_file.read() }')
    recipe_file.close()

    input('\nPresione ENTER para continuar...')
    system('cls')

def create_recipe():
    # Get and print categories list
    categories = list_from_dir(base_path)
    print_list(categories)

    # Select category
    ctgr_selected = -1
    while ctgr_selected not in range(1, len(categories) + 1):
        ctgr_selected = int(input('Elige la categoría: '))

    recipe_name = input('\n¿Cómo se llama el platillo?: ')
    recipe_name = f'{recipe_name}.txt'
    recipe_content = input('Escribe el contenido de la receta: ')

    # Create file and write content
    file_path = Path(base_path / categories[ctgr_selected-1] / recipe_name)
    recipe_file = open(file_path, 'w')
    recipe_file.write(recipe_content)
    recipe_file.close()

    print('\nReceta creada exitosamente!')
    input('Presione ENTER para continuar...')
    system('cls')

def create_category():
    category_name = input('\nNombre de nueva categoría: ')

    ctgr_path = Path(base_path / category_name)
    if not os.path.exists(ctgr_path):
        os.mkdir(ctgr_path)
        print('Categoría creada exitosamente!')
    else:
        print('Esa categoría ya existe...')

    input('Presione ENTER para continuar...')
    system('cls')

def delete_recipe():
    # Get and print categories list
    categories = list_from_dir(base_path)
    print_list(categories)

    # Select category
    ctgr_selected = -1
    while ctgr_selected not in range(1, len(categories) + 1):
        ctgr_selected = int(input('Elige la categoría: '))

    # Get and print recipes list
    recipes = list_from_dir(Path(base_path / categories[ctgr_selected - 1]))
    print_list(recipes)

    # Select recipe
    rcp_selected = -1
    while rcp_selected not in range(1, len(recipes) + 1):
        rcp_selected = int(input('Elige una receta: '))

    # Delete recipe
    file_path = Path(base_path / categories[ctgr_selected - 1] / recipes[rcp_selected - 1])
    os.remove(file_path)

    print('\nReceta eliminada exitosamente!')
    input('Presione ENTER para continuar...')
    system('cls')

def delete_category():
    # Get and print categories list
    categories = list_from_dir(base_path)
    print_list(categories)

    # Select category
    ctgr_selected = -1
    while ctgr_selected not in range(1, len(categories) + 1):
        ctgr_selected = int(input('Elige la categoría: '))

    ctgr_path = Path(base_path / categories[ctgr_selected - 1])
    os.rmdir(ctgr_path)

    print('\nCategoría eliminada exitosamente!')
    input('Presione ENTER para continuar...')
    system('cls')

option = -1
while option != 6:
    print('1. Leer receta\n2. Crear receta\n3. Crear categoría\n4. Eliminar receta\n5. Eliminar categoría\n6. Salir')
    option = int( input('Opción: ') )

    match option:
        case 1:
            read_recipe()
        case 2:
            create_recipe()
        case 3:
            create_category()
        case 4:
            delete_recipe()
        case 5:
            delete_category()
        case 6:
            break;
        case _:
            print('No es una entrada válida...\n')