def changeMarks(marks):
    result = []
    for mark in marks:
        if mark == 2: continue
        if mark == 3: result.append(4)
        else: result.append(mark)
    return result
one = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
two = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
three = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
print('Результат на 1-м списке:', changeMarks(one))
print('Результат на 2-м списке:', changeMarks(two))
print('Результат на 3-м списке:', changeMarks(three))