def getGap(id_tuple, idToFind):
    beginIndex = -1
    endIndex = 0
    index = 0
    for id in id_tuple:
        if id == idToFind:
            if beginIndex == -1:
                beginIndex = index
                endIndex = beginIndex
            else:
                endIndex += 1
                break
        if beginIndex != -1:
            endIndex += 1
        index += 1
    return tuple(list(id_tuple)[beginIndex:endIndex])

print(getGap((1, 2, 3), 8))
print(getGap((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(getGap((1, 2, 8, 5, 1, 2, 9), 8))