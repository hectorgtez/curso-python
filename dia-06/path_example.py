from pathlib import Path

base = Path.home()
guide = Path(base, 'Europa', 'España', Path('Barcelona', 'Sagrada_Familia.txt'))
guide2 = guide.with_name('La_Pedrera.txt')

print(guide)
print(guide2)