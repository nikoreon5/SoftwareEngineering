def unique_elements(lst):
    result = []
    for elem in lst:
        if not(elem in result):
            result.append(elem)
    return result
print('Тест 1:', unique_elements([]))
print('Тест 2:', unique_elements([1, 1, 1, 1, 1]))
print('Тест 3:', unique_elements([2, 1, 3, 4, 5, 6, 7, 2, 1, 3, 8]))