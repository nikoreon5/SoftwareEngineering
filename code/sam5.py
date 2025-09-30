list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
def toSet(myList):
    result = set()
    counts = {}
    for n in myList:
        counts[n] = counts.get(n, 0) + 1
    for n, count in counts.items():
        result.add(n)
        for i in range(2, count + 1):
            result.add(str(n) * i)
    return result

print(toSet(list_1))
print(toSet(list_2))
print(toSet(list_3))