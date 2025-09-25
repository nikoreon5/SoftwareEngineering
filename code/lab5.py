def useless(input_list):
    return max(input_list) / len(input_list)
print(useless([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]))
print(useless([1, 3, 9, 27, 81, 243, 729]))
print(useless([1, 5, 25, 125, 625]))