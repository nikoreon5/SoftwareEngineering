mySet = set('abcde')
print(mySet)
for i in range(1, 10):
    mySet.add(i)
print(mySet)

mySet = frozenset('abcde')
print(mySet)
for i in range(1, 10):
    mySet.add(i)
print(mySet)