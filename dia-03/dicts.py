dict1 = {'k1':'value1', 'k2':'value2'}

print(dict1)
print( type(dict1) )

result = dict1['k1']
print(result)

client = {'first_name':'Hector', 'last_name':'Gutierrez', 'weight':94, 'height':177}
consult = (client['height'])
print(f'{consult/100} m')

dict2 = {'k1':55, 'k2':[10, 20, 30], 'k3':{'s1':100, 's2':200}}
print(dict2['k2'][2])
print(dict2['k3']['s2'])

dict3 = {'k1':['a', 'b', 'c'], 'k2':['d', 'e', 'f']}
print(dict3['k2'][1].upper())

dict4 = {1:'a', 2:'b'}
print(dict4)

dict4[3] = 'c'
print(dict4)

print(dict4.keys())
print(dict4.values())
print(dict4.items())