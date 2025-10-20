arr = ['one', 'two', 'three']
with open('code/input.txt', 'w') as f:
    for line in arr:
        f.write(f'\nCycle run {line}')
    print('Done!')