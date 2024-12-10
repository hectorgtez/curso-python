from pathlib import Path, PureWindowsPath

folder = Path('D:/Documentos/Cursos/curso-python/dia-06/prueba.txt')

print(folder.read_text())
print(folder.name)
print(folder.suffix)
print(folder.stem)

if not folder.exists():
    print('Este archivo no existe...')
else:
    print('Nice! El archivo existe.')

windows_path = PureWindowsPath(folder)
print(windows_path)