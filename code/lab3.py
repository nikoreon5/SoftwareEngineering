def replace(input_list):
    memory = input_list[0]
    input_list[0] = input_list[-1]
    input_list[-1] = memory
    return input_list
print(replace([1, 2, 3, 4, 5]))

# альтернативное решение
def replace2(input_list):
    input_list[0], input_list[-1] = input_list[-1], input_list[0]
    return input_list
print(replace2([1, 2, 3, 4, 5]))