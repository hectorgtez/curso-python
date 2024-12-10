from pathlib import Path

# path = 'D:\\Documentos\\Cursos\\curso-python\\dia-06\\prueba2.txt'
# element = os.path.split(path)
# print(element)

folder = Path('D:/Documentos/Cursos/curso-python/dia-06')
file = folder / 'prueba.txt'

my_file = open(file)
print(my_file.read())

my_file.close()