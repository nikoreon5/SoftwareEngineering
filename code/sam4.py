sentence = input('Введите предложение на английском языке: ')

matches = 'aeiou'
count = 0
for letter in sentence:
    if letter in matches: count += 1

print(len(sentence))
print(sentence.lower())
print(f'Количество гласных: {count}')
print(sentence.replace('ugly', 'beauty'))
print('Предложение начинается с "The"' if sentence.startswith('The') else 'Предложение не начинается с "The"')
print('Предложение заканчивается "end"' if sentence.endswith('end') else 'Предложение не заканчивается "end"')