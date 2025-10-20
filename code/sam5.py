def test(filename, qa_separator):
    if len(filename) == 0 or len(qa_separator) == 0:
        print('Переданы некорректные параметры.')
        return
    points = 0
    with open(filename, 'r', encoding='utf-8') as f:
        qa = [line.rstrip().split(qa_separator) for line in f.readlines()]
        print(qa)
        if len(qa) != 0:
            print('Начнем тестирование.')
            for i in range(len(qa)):
                print(f'----- Вопрос {i + 1} ------')
                print(qa[i][0])
                ans = input('Ваш ответ: ')
                if ans == qa[i][1]:
                    print('Вы ответили верно!')
                    points += 1
                else:
                    print('Вы ошиблись. :(')
                    print(f'Верный ответ: {qa[i][1]}')
        print(f'Верных ответов: {points} из {len(qa)}')
test('code/input.txt', '/')