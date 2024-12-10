my_file = open('prueba.txt')

for line in my_file:
    print(line.rstrip())

my_file.close()