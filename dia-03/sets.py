set1 = set([1, 2, 3, 4, 5])
print(set1)
print( type(set1) )
print( len(set1) )

set2 = {1, 2, 3}
print(set2)
print( type(set2) )
print(2 in set2)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)
print(s3)

s1.add(4)
print(s1)

s1.remove(4)
s1.discard(100)
print(s1)