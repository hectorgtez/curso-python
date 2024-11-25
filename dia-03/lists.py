my_list = ['a', 'b', 'c']
my_list2 = ['d', 'e', 'f']
disordered_list = ['g', 'o', 'b', 'm', 'c']

print( type(my_list) )
print( len(my_list) )
print( my_list[0:1] )
print( my_list + my_list2 )

my_list[0] = 'alfa'
print(my_list)
my_list[0] = 'a'

my_list.append('d')
print(my_list)

deleted = my_list.pop(2)
print(my_list)
print(deleted)

disordered_list.sort()
print(disordered_list)

disordered_list.reverse()
print(disordered_list)